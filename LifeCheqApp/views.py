from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from .models import Input, Output
from django.db.models import Sum
from .forms import InputForm
from . import plots
import plotly.graph_objects as go
import plotly.offline as plt


def index(request):
    context = {}
    return render(request, 'LifeCheqApp/index.html', context)


def inputView(request):
    if request.method != 'POST':
        form = InputForm()
    else:
        form = InputForm(data=request.POST)
        if form.is_valid:
            instance = form.save()
            return redirect(reverse('LifeCheqApp:output', args=(instance.pk,)))
    context = {'form': form}
    return render(request, 'LifeCheqApp/input.html', context)


def outputView(request, loan_number):
    context = {}
    context['object'] = Input.objects.get(pk=loan_number)
    context['total_payment'] = Output.objects.filter(loan_number=loan_number).aggregate(total=Sum('payment_period'))
    context['total_interest'] = Output.objects.filter(loan_number=loan_number).aggregate(total=Sum('interest_period'))
    return render(request, 'LifeCheqApp/output.html', context)


def outputsView(request):
    context = {}
    context['objects'] = Input.objects.order_by('-loan_number')
    return render(request, 'LifeCheqApp/outputs.html', context)


def outputTable(request, loan_number):
    context = {}
    context['objects'] = Output.objects.filter(loan_number=loan_number)
    return render(request, 'LifeCheqApp/table.html', context)


def plotView(request, loan_number):

    period = list(range(1,int(Input.objects.get(pk = loan_number).term*12)+1))
    interest = [object.interest_period for object in Output.objects.filter(loan_number = loan_number)] 
    principal = [object.principal_period for object in Output.objects.filter(loan_number = loan_number)]
    
 
    fig = go.Figure(data=[ go.Bar(name='Interest', x=period, y=interest, marker_color='rgb(242,89,82)'),
                    go.Bar(name='Principal', x=period, y=principal, marker_color='rgb(13,196,163)')])

    fig.update_layout(
                    title='Interest and Principal payments per period',
                    yaxis=dict(title='Amount', titlefont_size=16, tickfont_size=14,),
                    xaxis=dict(title='Period', titlefont_size=16, tickfont_size=14,),
                    barmode='stack')

    context = {}
    context['plot'] = plt.plot(fig, output_type='div', include_plotlyjs=False)

    return render(request, 'LifeCheqApp/plot.html', context)


# CLASS_BASED PLOTTING VIEW
# class Visualisation(TemplateView) :
#     template_name = 'LifeCheqApp/plots.html'

#     def get_context_data(self, **kwargs):
#         context = super(Visualisation, self).get_context_data(**kwargs)
#         context['plot'] = plots.get_Bar()
#         context['record'] = plots.get_record_number()
#         return context

#     def get_record_number(self, loan_number):
#         latest_record_id = Input.objects.get(loan_number=loan_number)
#         return latest_record_id