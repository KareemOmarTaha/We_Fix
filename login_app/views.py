from django.shortcuts import render

def log_in(request):
    return render(request , 'login.html')