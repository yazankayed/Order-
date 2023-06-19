from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login_page', views.login_page),
    path('register_page', views.register_page),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('complian',views.complain),
    path('savecomplian',views.savecomplian),
    path('displaycomplain',views.displaycomplain)
]
