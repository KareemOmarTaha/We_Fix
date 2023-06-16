from django.urls import path 
from . import views
urlpatterns = [
    path('loging-in' , views.log_in )
]
