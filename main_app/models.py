from django.db import models
from login_app.models import User

class Category(models.Model):
    name = models.CharField(max_length=45)

class Freelancer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=10)
    experience = models.IntegerField(default=0)
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
    user.address = request.POST['address']
    user.phone_number = request.POST['phone']
    user.save()



def delete_user(request):
    user = User.objects.get(id = request.session['userid'])
    user.delete()

def show_all_users_models():
    return User.objects.exclude(id = 1)

def user_profile_models(id):
    return User.objects.get(id = id)

def admin_edit_models(request):
    user = User.objects.get(id = request.POST['user_id'])
    user.first_name = request.POST['fname']
    user.last_name = request.POST['lname']
    user.email = request.POST['email']
    user.address = request.POST['address']
    user.phone_number = request.POST['phone']
    user.save()

def admin_delete_user(request , id):
    user = User.objects.get(id = id)
    user.delete()

def add_freelancer_models(request):
    Freelancer.objects.create(first_name = request.POST['fname'] , last_name = request.POST['lname'] , 
                            phone_number = request.POST['phone'] , experience = request.POST['exp']
                            , category = Category.objects.get( name = request.POST['category'] ))
    

def show_freelancer_models():
    a = [1,3,4,5,6,7]
    return Freelancer.objects.exclude(id__in = a)

def delete_freelancer_models(request , id):
    freelancer = Freelancer.objects.get(id = id)
    freelancer.delete()

def edit_freelancer( id):
    return Freelancer.objects.get(id = id)

def editing_freelance_models(request):
    freelancer = Freelancer.objects.get (id = request.POST['freelancer_id'])
    freelancer.first_name = request.POST['fname']
    freelancer.last_name = request.POST['lname']
    freelancer.phone_number = request.POST['phone']
    freelancer.experience = request.POST['exp']
    freelancer.category = Category.objects.get(name = request.POST['category'])
    freelancer.save()

def category_modles():
    return Category.objects.all()

def list_cat_models(id):
    return Freelancer.objects.filter(category = Category.objects.get(id=id))