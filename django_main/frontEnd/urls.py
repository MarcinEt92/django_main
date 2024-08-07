"""
URL configuration for zelentDjango project.

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
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="frontend_index"),
    path("html_tutorial/", views.html_tutorial, name='html_tutorial'),
    path("css_tutorial/", views.css_tutorial, name='css_tutorial'),
    path("js_tutorial/", views.js_tutorial, name='js_tutorial'),
    path("<slug:tutorial_name>/<int:tutorial_id>/", views.tutorial_generic, name='tutorial_generic'),
    path("frames/<slug:tutorial_name>/<int:tutorial_id>/", views.frames, name='frames'),
]
