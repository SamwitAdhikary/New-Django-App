from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('contact', views.contact, name='Contact'),
    path('search', views.search, name='Search'),
]