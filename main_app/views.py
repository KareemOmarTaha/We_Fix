from django.shortcuts import render , redirect

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
