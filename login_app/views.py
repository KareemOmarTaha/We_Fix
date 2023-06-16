from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from .models import User
import bcrypt


def index(request):
    return render(request,'index.html')

def register(request):
    errors = User.objects.register(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        models.register(request)
        return redirect('/')


def login(request):
    user = User.objects.filter(email = request.POST['person_email'])
    if user :
        logged_user = user[0]
    
        if bcrypt.checkpw(request.POST['password_email'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id

            return redirect('/')
    return redirect('/login')

def show(request):
    if 'userid' not in request.session:
        return redirect('/login')
    else:
        return render(request,'welcome.html')

