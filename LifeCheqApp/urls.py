from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'LifeCheqApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.inputView, name='input'),
    path('output/<int:loan_number>', views.outputView, name='output'),
    path('output/table-<int:loan_number>', views.outputTable, name='table'),
    path('output/all', views.outputsView, name='outputs'),
    path('admin/', admin.site.urls),
]