from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_form, name='event_form'),
    path('event_organized', views.one, name='event_organized'),
    ]
