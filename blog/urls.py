from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.blog, name='BlogHome'),
    path('<str:slug>', views.blogpost, name='BlogHome'),
]