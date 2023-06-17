from django.db import models
import re
import bcrypt
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        x = User.objects.filter(email=postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['fname']) < 2:
            errors["fname"] = "First Name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "last Name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password description should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors["confirm_password"] = "Password conformation didn't match"
        if len (x) > 0 :
            errors['emaill'] = "Email Already Used!"
        return errors


class Company(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company_logo=models.CharField(max_length=45,default="nothing")


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, related_name="item", on_delete = models.CASCADE)
    objects = UserManager()



def show_companies():
    return Company.objects.all()





def register(request):
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(first_name = request.POST['fname'] ,last_name = request.POST['lname'] , email = request.POST['email'] , password= pw_hash,company_id = request.POST['company'] )
    

def login(request):
    user = User.objects.get(email = request.POST['email'])
    if user :
        logged_user = user.email
    
    if bcrypt.checkpw(request.POST['password_email'].encode(), logged_user.password.encode()):
        request.sessuion['userid'] = logged_user.id

