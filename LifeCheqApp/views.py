from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import TemplateView
from .models import InModel, OutModel
from .forms import InForm
# from . import plots


def index(request):
    context = {}
    return render(request, 'LifeCheqApp/index.html', context)


def inView(request):
    if request.method != 'POST':
        form = InForm()
    else:
        form = InForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('LifeCheqApp:record')
    context = {'form': form}
    return render(request, 'LifeCheqApp/input.html', context)


def recordView(request):
    context = {}
    context['object'] = InModel.objects.all().last()
    return render(request, 'LifeCheqApp/record.html', context)


def recordTable(request):
    context = {}
    context = OutModel.objects.last()

    return render(request, 'LifeCheqApp/table.html', context)


def recordsView(request):
    context = {}
    context = InModel.objects.order_by('-date').values()
    return render(request, 'LifeCheqApp/records.html', context)


# class Visualisation(TemplateView):
#     template_name = 'LifeCheqApp/plots.html'

#     def get_context_data(self, **kwargs):
#         context = super(Visualisation, self).get_context_data(**kwargs)
#         context['object'] = plots.get_Bar()
#         return context
