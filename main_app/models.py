from django.db import models
from login_app.models import User

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


def user_info(request):
    return User.objects.get(id = request.session['userid'])

def edit_user_info(request):
    user = User.objects.get(id = request.session['userid'])
    user.first_name = request.POST['fname']
    user.last_name = request.POST['lname']
    user.email = request.POST['email']
    user.address = request.POST['phone']
    user.save()

def delete_user(request):
    user = User.objects.get(id = request.session['userid'])
    user.delete()