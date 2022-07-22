from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.pest ,name='pest'),
    path('cam/',views.pestcam ,name='pestcam')

]
