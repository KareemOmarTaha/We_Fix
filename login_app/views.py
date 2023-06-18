from django.shortcuts import render, redirect , HttpResponse
from . import models
from django.contrib import messages
from .models import User
import bcrypt

def log_in(request):
    return render(request , 'login.html')


def register(request):
    errors = User.objects.register(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/log-in')
    else:
        models.register(request)
        return redirect('/log-in')
    


def logining(request):
    message = User.objects.login(request.POST)
    if len(message) > 0:
        for key, value in message.items():
            messages.error(request, value)
        return redirect('/log-in')
    else:
        user = User.objects.filter(email = request.POST['person_email'])
    if user :
        logged_user = user[0]
    
        if bcrypt.checkpw(request.POST['password_email'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            if logged_user.id == 1: 
                return redirect ('/admin')
            else:
                return redirect('/')
    return redirect('/log-in')


def admin(request):
    if 'userid' not in request.session:
        return redirect ('/')
    if request.session['userid'] == 1 : 
        return render (request , 'admin.html')
    else:
        return redirect('/')
    

# def create(request):
#     if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         password = request.POST['password']
#         phone = request.POST['phone']
#         address = request.POST['address']

#         new_user = User(first_name = fname , last_name = lname , email = email , password= password , phone_number= phone , address = address )
#         new_user.save()
#         success = 'Account Registered Successfully ' + fname 
#         return HttpResponse(success)
