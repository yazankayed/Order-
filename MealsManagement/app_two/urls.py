from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home),
    path('startvote', views.startvote),
    path('voting', views.voting),
    path('submitvote/<int:ic>', views.submitvote),
    path('thewinner', views.thewinner),
    path('addacompanypage', views.add_a_company),
    path('addacompany', views.addacompany),
    path('addarestpage', views.add_a_rest),
    path('addarest', views.addarest),
    path ('message' , views.create_msg),
    path('contactus', views.contactus),
    path('rest/<int:id>', views.restdet),
    path ('search/' , views.Serach_Request),
    path ('contact' , views.contact),
    path ('about' , views.about),  
    
    
]
