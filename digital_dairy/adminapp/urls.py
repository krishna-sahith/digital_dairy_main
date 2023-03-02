from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_profile, name='admin_profile_form'),
    path('admin_profile_form', views.one, name=''),
]
