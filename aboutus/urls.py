from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.aboutus ,name='aboutus'),
    path('contact/',views.contact, name='contact')
]
