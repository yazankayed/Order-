from django.contrib import admin
# from .models import Restaurant
from app_two.models import Restaurant,Company,Item,Menu
admin.site.register(Restaurant)
admin.site.register(Company)
admin.site.register(Item)
admin.site.register(Menu)
# Register your models here.
