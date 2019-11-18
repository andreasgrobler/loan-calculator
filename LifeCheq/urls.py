from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('LifeCheqApp.urls')),
    path('admin/', admin.site.urls),
]
