from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'LifeCheqApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.inView, name='input'),
    path('record/', views.recordView, name='record'),
    path('record/all', views.recordsView, name='records'),
    path('record/table', views.recordTable, name='table'),
    path('admin/', admin.site.urls),
]