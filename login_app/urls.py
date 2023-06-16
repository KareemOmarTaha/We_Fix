from django.urls import path
from . import views
urlpatterns = [
    path('login', views.index),
    path('login/register', views.register),	
    path('dashboard', views.show),	
    path('logedin', views.login),	
    
]