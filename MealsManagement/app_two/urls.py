from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home),
    path('startvote', views.startvote),
    path('voting', views.voting),
    path('submitvote//<int:ic>', views.submitvote),
    path('thewinner', views.thewinner),
    path('addacompanypage', views.add_a_company),
    path('addacompany', views.addacompany),
    path('addarestpage', views.add_a_rest),
    path('addarest', views.addarest),
    
]
