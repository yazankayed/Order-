from django.shortcuts import render,redirect,HttpResponse
from . import models

# Create your views here.
def home(request):
    return render(request,'home.html')

def startvote(request):
    if 'userid' not in request.session:
        return redirect('/')
    if 'startvote' in request.session:
        return redirect('/voting')
    else:
        request.session['startvote'] = 1
        context={
            'show_all_resturants': models.show_all_resturants(),
            "logged_user" : models.get_specific_user(request),
        }
        return render(request, 'vote.html',context)

def voting(request):
    request.session['startvote'] =1
    context={
        'show_all_resturants': models.show_all_resturants(),
        "logged_user" : models.get_specific_user(request),
        "msg": models.show_msg()
    }
    return render(request,'voting_page.html',context)

def submitvote(request,ic):
    models.voting(request,ic)
    return redirect('/voting')


def create_msg(request):
    models.create_message(request)
    return redirect('/voting')


def thewinner(request):
    if 'startvote' not in request.session:
        return redirect('/startvote')
    else:
        del request.session['startvote']
        models.Restaurant.users_who_voted.through.objects.all().delete()
        msg=models.Message.objects.all()
        rest = models.Restaurant.objects.all()
        for mseg in msg : 
            mseg.delete()
        for res in rest : 
            res.votes=0
            res.save()
    # b.users_who_voted.aclear()
        context={
            'the_winner_rest': models.get_the_winner_rest(request)[0],
            "logged_user" : models.get_specific_user(request),
        }
        return render(request,'thewinner.html',context)





def add_a_company(request):
    return render (request,'addcompanypage.html')

def addacompany(request):
    models.add_a_company(request)
    return redirect('/addacompanypage')

def add_a_rest(request):
    return render (request,'addarest.html')

def addarest(request):
    models.add_a_rest(request)
    return redirect('/addarestpage')