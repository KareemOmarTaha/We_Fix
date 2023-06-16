from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=45)

class Freelancer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    experience = models.IntegerField()
    category = models.ForeignKey(Category , related_name="freelancers" , on_delete=models.DO_NOTHING )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


