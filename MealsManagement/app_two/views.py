from django.shortcuts import render,redirect,HttpResponse
from . import models

# Create your views here.
def home(request):
    return render(request,'home.html')

def startvote(request):
    canstartvote=request.session['startvote']
    if canstartvote:
        return redirect('/voting')
    else:
        context={
            'show_all_resturants': models.show_all_resturants(),
            "logged_user" : models.get_specific_user(request),
        }
        return render(request, 'vote_test.html',context)

def voting(request):
    request.session['startvote'] =1
    context={
        'show_all_resturants': models.show_all_resturants(),
        "logged_user" : models.get_specific_user(request),
    }
    return render(request,'voting_page.html',context)

def submitvote(request,ic):
    models.voting(request,ic)
    return redirect('/voting')


def thewinner(request):
    del request.session['startvote']
    context={
        'the_winner_rest': models.get_the_winner_rest(),
        "logged_user" : models.get_specific_user(request),
    }
    return render(request,'thewinner.html',context)