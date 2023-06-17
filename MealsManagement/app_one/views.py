from django.shortcuts import render, redirect,HttpResponse
from . import models
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request,'index.html')
def login_page(request):
    return render(request,'login_page.html')
def register_page(request):
    context = {
        "company_name" : models.show_companies(),
        
    }
    return render(request,'reg.html',context)

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register_page')
    else:
        models.register(request)
        return redirect('/login_page')

def login(request):
    user = User.objects.filter(email = request.POST['person_email'])
    if user :
        logged_user = user[0]
    
        if bcrypt.checkpw(request.POST['password_email'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/startvote')
    return redirect('/login_page')

def logout(request):
    del request.session['userid']
    return redirect('/')
