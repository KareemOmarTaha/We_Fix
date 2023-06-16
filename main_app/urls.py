
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index ),
    path('home' , views.home),
    path ('category', views.category),
    path ('about-us' , views.about_us),
    path ('login' , views.login),
]
