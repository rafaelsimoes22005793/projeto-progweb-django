"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = 'portfolio'


urlpatterns = [
    path('', views.index_view),
    path('admin/', admin.site.urls),
    path('index', views.index_view, name='index'),
    path('projetos', views.projetos_view, name='projetos'),
    path('contactos', views.contactos_view, name='contactos'),
    path('jsplayground', views.jsplayground_view, name='JSPlayground'),
    path('blog', views.blog_view, name='blog'),
    path('sobre', views.sobre_view, name='sobre'),
    path('aboutme', views.aboutme_view, name='aboutme'),
    
]
