from django.shortcuts import render, redirect, get_object_or_404
from .models import Login
from .forms import LoginForm
from django.http import HttpResponse
from django.template import loader



def index(request):
    template = loader.get_template('movie_admin/index.html')
    print("here")
    return HttpResponse(template.render(request))

def enter(request):
    print("hhksl")
    count_admins = Login.objects.raw('Select count(*) form movie_admin_login')
    print(count_admins)
    template1 = loader.get_template('movie_admin/signup.html')
    template2 = loader.get_template('movie_admin/login.html')
    if count_admins==0:
        return HttpResponse(template1.render(request))
    return HttpResponse(template2.render(request))

def login(request):
        if request.method == "POST":
            print(request.data)
            template = loader.get_template('movie_admin/index.html')
            print("here")
            return HttpResponse(template.render(request))