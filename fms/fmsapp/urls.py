from django import views
from django.conf import settings
from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('upload/',views.upload,name='upload'),
    path('books/',views.book_list,name='book_list'),
    path('books/upload/',views.upload_book,name='upload_book'),
    path('books/<int:pk>/',views.delete_book,name='delete_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
