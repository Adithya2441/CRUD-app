from django import views
from django.conf import settings
from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('upload/',views.upload,name='upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
