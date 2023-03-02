from django.urls import path
from . import views

urlpatterns = [
    path('', views.fdp_form, name='fdp_form'),
    path('fdp_form', views.one, name=''),
]
