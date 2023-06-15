from django.shortcuts import render, redirect,HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")



