
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index ),
    path('home' , views.home),
    path ('category', views.category),
    path ('about-us' , views.about_us),
    path ('login' , views.login),
    path('logout' , views.logout) ,
    path('profile' , views.show_profile) ,
    path ('editprofile' , views.edit_profile),
    path ('deleteuser' , views.delete_user),
]
