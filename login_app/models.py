from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register(self, postData):

        #RegEx for email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #RegEx for Password
        PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d,!@#$%^&*+=]{8,}$')

        FISRT_NAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$')

        LAST_NAME_REGEX = re.compile(r'^[a-zA-Z0-9]+$')

        errors = {}

        # Validating Email
        if len(postData['email']) < 1:
            errors['email'] = 'Email is required!'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email-invalid'] = 'Invalid Email!'
        check = User.objects.filter(email=postData['email'].lower())
        if len(check) > 0:
            errors['email-inuse'] = 'Email already in use!'

        # Validating Password
        if len(postData['password']) < 1:
            errors['password'] = 'Password is required!'
        elif not PASSWORD_REGEX.match(postData['password']):
            errors['password_valid'] = 'Password must contain at least 8 characters and capitalization!'

        if len(postData['confirm_password']) < 8:
            errors['password_confirm'] = 'Confirm password is required!'
        elif postData['confirm_password'] != postData['password']:
            errors['passwords_match'] = 'Password must match Confirm password!'
        
        # Validating First Name 
        if len(postData['fname']) < 3:
            errors["fname"] = "First name should be at least 3 characters"
        elif not FISRT_NAME_REGEX.match(postData['fname']):
            errors["fname"] = "First Name only conatains letter"
        
        # Validating Last Name
        if len(postData['lname']) < 3:
            errors["lname"] = "Last Name should be at least 3 characters"
        elif not LAST_NAME_REGEX.match(postData['lname']):
            errors["lname"] = "Last Name only conatains letter"

        return errors

# Login Validation

    def login(self, postData):
        messages = {}

        if len(postData['person_email']) < 1:
            messages['person_email'] = 'Email is required!'

        if len(postData['password_email']) < 1:
            messages['password_email'] = 'Password is required!'

        return messages

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=45 , default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


def register(request):
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name = request.POST['fname'] ,last_name = request.POST['lname'] , email = request.POST['email'] , 
                        password= pw_hash ,phone_number = request.POST['phone'] , address = request.POST['address'] )
    