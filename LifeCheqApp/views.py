from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, reverse
from django.views.generic import TemplateView
from .models import Input, Output
from django.db.models import Sum
from .forms import InputForm
from . import plots


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


class Visualisation(TemplateView) :
    template_name = 'LifeCheqApp/plots.html'

    def get_context_data(self, **kwargs):
        context = super(Visualisation, self).get_context_data(**kwargs)
        context['plot'] = plots.get_Bar()
        context['record'] = plots.get_record_number()
        return context

    def get_record_number(self, loan_number):
        latest_record_id = Input.objects.get(loan_number=loan_number)
        return latest_record_id