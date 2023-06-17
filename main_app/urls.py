
from django.urls import path 
from . import views

urlpatterns = [
    path ('', views.index ),
    path ('home' , views.home),
    path ('category', views.category),
    path ('about-us' , views.about_us),
    path ('login' , views.login),
    path ('logout' , views.logout),
    path ('profile' , views.show_profile) ,
    path ('editprofile' , views.edit_profile),
    path ('deleteuser' , views.delete_user),
    path ('userslist' , views.show_all_users),
    path ('userprofile/<int:id>' , views.show_user_profile) ,
    path ('adminedit' , views.admin_edit) ,
    path ('admindelete/<int:id>' , views.admin_delete) ,
    path ('registerfreelancer' , views.register_freelancer) , 
    path ('addfreelancer' , views.add_freelancer),
    path ('showfreelancer' , views.show_freelancer),
    path ('deletefreelancer/<int:id>' , views.delete_freelancer) , 
    path ('editfreelancer/<int:id>' , views.edit_freelancer),
    path ('editingfreelancer' , views.editing_freelancer),
    path ('category/<int:id>' , views.list_cat) , 
]
