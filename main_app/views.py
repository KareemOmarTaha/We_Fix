from django.shortcuts import render , redirect
from . import models

def index (request):
    return render(request , "home.html")

def home (request):
    return redirect ('/')

def category (request):
    return redirect('/')

def about_us (request):
    return redirect ('/')

def login (request):
    return redirect ('/log-in')

def logout(request):
    del request.session['userid']
    return redirect('/')

def show_profile(request):
    if 'userid' not in request.session:
        return redirect('/login')
    else:
        context = {
        "users" : models.user_info(request)
    }
        return render(request , 'profile.html' , context)


def edit_profile (request):
    models.edit_user_info(request)
    return redirect('/profile')

def delete_user(request):
    models.delete_user(request)
    return redirect('/logout')