from django.shortcuts import render , redirect
from . import models

def index (request):
    if 'userid' not in request.session:
        return render(request , "home.html")
    if request.session['userid'] == 1:
        return redirect ('/admin')
    else:
        return render(request , "home.html")

def home (request):
    if 'userid' not in request.session:
        return redirect('/')
    if request.session['userid'] == 1:
        return redirect ('/admin')
    else: 
        return redirect ('/')

def category (request):
    if 'userid' not in request.session:
        return redirect('/')
    else: 
        context = {
            "categories" : models.category_modles() ,

        }
        return render (request , 'categories.html' , context)
    
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

def show_all_users(request):
    if 'userid' not in request.session:
        return redirect ('/')
    if request.session['userid'] == 1:
        context = {
        "users" : models.show_all_users_models()
    }
        return render (request , "allusers.html" , context)
    else:
        return redirect ('/')

def show_user_profile(request , id):
    if 'userid' not in request.session:
        return redirect ('/')
    if request.session['userid'] == 1:
        context = {
        "users" : models.user_profile_models(id)
    }
        return render (request , "adminedit.html" , context)
    else:
        return redirect ('/')
    

def admin_edit(request):
    models.admin_edit_models(request)
    return redirect('/')

def admin_delete(request , id):
    models.admin_delete_user(request , id)
    return redirect('/userslist')

def register_freelancer (request):
    if 'userid' not in request.session:
        return redirect ('/')
    if request.session['userid'] == 1:
        return render (request , "addfreelancer.html")
    else:
        return redirect ('/')

def add_freelancer(request):
        
        models.add_freelancer_models(request)
        return redirect('/')


def show_freelancer(request):
    if 'userid' not in request.session:
        return redirect ('/')
    if request.session['userid'] == 1:
        context = {
            "freelancers" : models.show_freelancer_models()
        }
        return render (request , "showfreelancer.html" , context)
    else:
        return redirect ('/')
    
def delete_freelancer(request , id):
    models.delete_freelancer_models(request , id)
    return redirect('/showfreelancer')

def edit_freelancer(request , id):
    context = {
    "freelancers" :models.edit_freelancer(id)
    }
    return render (request , 'editfreelancer.html' , context)

def editing_freelancer (request):
    models.editing_freelance_models(request)
    return redirect ('/showfreelancer')

def list_cat(request , id):
    if 'userid' not in request.session:
        return redirect('/')
    else:
        context = {
    "all_cats":models.list_cat_models(id)
    }
        return render (request , "list-cat.html" , context)