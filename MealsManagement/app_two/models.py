from django.db import models
from app_one.models import User
from app_one.models import Company
from django.db.models import Max


class Restaurant(models.Model):
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    telephone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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



def get_specific_user(request):
    return User.objects.get(id=request.session['userid'])

def show_all_resturants():
    return Restaurant.objects.all()

def show_specific_restaurant(ic):
    return Restaurant.objects.get(id=ic)

def show_specific_company(num):
    return Company.objects.get(id=num)

def show_all_company():
    return Company.objects.all()

def voting(request,ic):
    rest_to_update=Restaurant.objects.get(id=request.POST['vote_id'])
    rest_to_update.votes= rest_to_update.votes+1
    rest_to_update.save()
    cc=Restaurant.objects.get(id=request.POST['vote_id'])
    user = User.objects.get(id=request.session['userid'])
    user.liked_rest.add(cc)
    return

def get_the_winner_rest(request):
    most_voted_restaurant = Restaurant.objects.aggregate(Max('votes'))
    max_votes = most_voted_restaurant['votes__max']
    most_voted_restaurants = Restaurant.objects.filter(votes=max_votes)
    return most_voted_restaurants[0]

def add_a_company(request):
    Company.objects.create(name=request.POST['company_name'],company_logo=request.POST['logo_company'])

def add_a_rest(request):
    Restaurant.objects.create(name=request.POST['rest_name'],location=request.POST['rest_location'],telephone_number=request.POST['rest_telephone'],rest_logo=request.POST['logo_rest'])

