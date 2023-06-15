from django.db import models
from app_one.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    telephone_number = models.CharField(max_length=10)
    votes = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    votes= models.IntegerField(default=0)
    users_who_voted= models.ManyToManyField(User, related_name="liked_rest")


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




