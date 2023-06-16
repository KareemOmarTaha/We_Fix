from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=10)
    address = models.CharField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

