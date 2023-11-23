"""
URL configuration for Vanuishin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from Nikita import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Contacks/', views.Contacks, kwargs = {'Contacks' : 'NikitaVan12'}),
    path('about/', views.about, kwargs = {'resp' : 'Bashkirya', 'city' : 'Nsk'}),
    path('full_name/', views.full_name, kwargs={'name': 'NIKITOS', 'age': 22, 'interesting': 'Python'})
]
