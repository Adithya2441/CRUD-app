from django import views
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
]