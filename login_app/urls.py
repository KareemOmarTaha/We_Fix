from django.urls import path 
from . import views
urlpatterns = [
    path('log-in' , views.log_in ) , 
    path ('register' , views.register) , 
    path ('loging-in' , views.logining) , 
    path ('admin' , views.admin)
]
