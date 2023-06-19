from django.shortcuts import render , redirect
from . import models
from login_app.models import User
from main_app.models import Freelancer
from django.contrib import messages
from django.http import JsonResponse
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
    errors = Freelancer.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registerfreelancer')
    else:
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
    context = {
    "all_cats":models.list_cat_models(id)
    }
    return render (request , "list-cat.html" , context)

def free_details(request , id):
    if 'userid' not in request.session:
        return redirect ('/log-in')
    else:
        context = {
        "free_details" : models.free_details_models(id)
    }
        return render (request , 'free-details.html', context)

def like_freelancer(request, id):
        logged_user = User.objects.get(id = request.session['userid'])
        liked_freelancer = Freelancer.objects.get(id = id)
        if liked_freelancer in logged_user.liked_freelancer.all():
            logged_user.liked_freelancer.remove(liked_freelancer)
        else:
            logged_user.liked_freelancer.add(liked_freelancer)
        if liked_freelancer in logged_user.disliked_freelancer.all():
            logged_user.disliked_freelancer.remove(liked_freelancer)
        return redirect(f'/freedetails/{liked_freelancer.id}')

def dislike_freelancer(request, id):
        logged_user = User.objects.get(id = request.session['userid'])
        disliked_freelancer = Freelancer.objects.get(id = id)
        if disliked_freelancer in logged_user.disliked_freelancer.all():
            logged_user.disliked_freelancer.remove(disliked_freelancer)
        else:
            logged_user.disliked_freelancer.add(disliked_freelancer)
        if disliked_freelancer in logged_user.liked_freelancer.all():
            logged_user.liked_freelancer.remove(disliked_freelancer)
        return redirect(f'/freedetails/{disliked_freelancer.id}')


def contact_us (request):
    
    return render(request , 'Contactus.html')

def about_us (request):
    return render (request , 'aboutUS.html')



def Serach_Request(request):
    if request.is_ajax():
        freelancer = request.POST.get('freelancer')
        print(freelancer)
        query = Freelancer.objects.filter(first_name__icontains=freelancer)
        if len(query) > 0 :
            data = [] 
            for position in query:
                Items = {
                    "PRIMARY_KEY" :position.pk,
                    "first_name" : position.first_name,
                    "phone" : position.phone_number,
                    "image_category":position.category.image
                    
                }
                data.append(Items)
            res = data
        else:
            res = 'NO Freelancer Found....'
                
        return JsonResponse({'data': res })
    return JsonResponse({})