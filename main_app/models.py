from django.db import models
from login_app.models import User


class Category(models.Model):
    name = models.CharField(max_length=45)

class Freelancer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=45)
    experience = models.IntegerField()
    rating = models.ManyToManyField(User , related_name="freelancers")
    rate = models.IntegerField(default=0)
    category = models.ForeignKey(Category , related_name="freelancers" , on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

