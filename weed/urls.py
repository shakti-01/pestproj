from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.weed ,name='weed'),
    path('cam/',views.weedcam, name='weedcam')
]
