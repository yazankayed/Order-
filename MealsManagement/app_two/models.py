from django.db import models
from app_one.models import User
from app_one.models import Company
from django.db.models import Max

class Restaurant(models.Model):
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    telephone_number = models.CharField(max_length=10)
    votes= models.IntegerField(default=0)
    users_who_voted= models.ManyToManyField(User, related_name="liked_rest")
    rest_logo=models.CharField(max_length=45,default="nothing")


class Menu(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    restaurant = models.OneToOneField(Restaurant,related_name="menu", on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    menue = models.ForeignKey(Menu, related_name="item", on_delete = models.CASCADE)

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User , related_name="messages" , on_delete=models.DO_NOTHING)


def get_specific_user(request):
    return User.objects.get(id=request.session['userid'])

def show_all_resturants():
    return Restaurant.objects.all()

def show_specific_restaurant(id):
    return Restaurant.objects.get(id=id)

def show_specific_company(num):
    return Company.objects.get(id=num)

def show_all_company():
    return Company.objects.all()

def voting(request,ic):
    rest_to_update=Restaurant.objects.get(id=ic)
    rest_to_update.votes= rest_to_update.votes+1
    rest_to_update.save()
    cc=Restaurant.objects.get(id=ic)
    user = User.objects.get(id=request.session['userid'])
    user.liked_rest.add(cc)

def get_the_winner_rest(request):
    return Restaurant.objects.all().order_by('-votes')[0]
def add_a_company(request):
    Company.objects.create(name=request.POST['company_name'],company_logo=request.POST['logo_company'])

def add_a_rest(request):
    Restaurant.objects.create(name=request.POST['rest_name'],location=request.POST['rest_location'],telephone_number=request.POST['rest_telephone'],rest_logo=request.POST['logo_rest'])


def create_message(request):
    this_message = request.POST['post_message']
    this_user = User.objects.get(id = request.session['userid'])
    Message.objects.create(message = this_message ,   user = this_user)


def show_msg():
    return Message.objects.all().order_by("created_at")


