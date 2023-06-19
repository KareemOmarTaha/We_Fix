from django.db import models
from login_app.models import User
import re

class FreelancerManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        Phone_REGEX = re.compile(r'^[0-9]+$')
        
        if len(postData['fname']) < 3:
            errors["fname"] = "Freelancer first name should be at least 3 characters"
        if len(postData['lname']) < 3:
            errors["lname"] = "Freelancer last name should be at least 3 characters"
        if len(postData['phone']) != 10:
            errors["phone"] = "Phone Number Should contain 10 numbers"
        if not Phone_REGEX.match(postData['phone']):
            errors['email'] = "Invalid Phone Number!"
        if postData['exp'] < "0" :
            errors["exp"] = "Invalide number of experience years"
        return errors


class Category(models.Model):
    name = models.CharField(max_length=45)
    image = models.CharField(max_length=255 , default='yes')

class Freelancer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=10)
    experience = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category , related_name="freelancers" , on_delete=models.DO_NOTHING )
    users_who_like = models.ManyToManyField(User, related_name='liked_freelancer')
    users_who_dislike = models.ManyToManyField(User, related_name='disliked_freelancer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FreelancerManager()

class ContactUs(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    message = models.TextField(max_length=45)


class complaint(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    complaint = models.CharField(max_length=255)

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
    a = [1,3,4,5,6,7]
    return Freelancer.objects.filter(category = Category.objects.get(id=id)).exclude(id__in = a)

def free_details_models(id):
    return Freelancer.objects.get(id = id)
    
def contactus_form(request):
    ContactUs.objects.create(first_name = request.POST['fname'] , last_name = request.POST['lname'], email = request
    .POST['email'], message= request.POST['message'])
    
def complaint_models(request):
    complaint.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], complaint= request.POST['complaint'])
