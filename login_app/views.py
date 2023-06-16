from django.shortcuts import render, redirect
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

            return redirect('/')
    return redirect('/log-in')