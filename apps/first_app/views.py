from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from datetime import datetime
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'[A-Za-z]{1,10} ?[A-Za-z]{0,10}$')

def index(request):
    return render(request, 'index.html')

def register(request):
    # errors = User.objects.validation(request.POST)
    errors = User.objects.validation(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    else: 
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(user_name=request.POST['user_name'],first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash)
        request.session['user_name'] = request.POST['user_name']
        return redirect('/')
    


def login(request):
    
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['user_name'] = User.objects.get(email=request.POST['loginmail']).first_name
        return redirect('/result')

def result(request):
    return render(request, 'result.html')



# def passwordReset(request):
#     return render(request, 'password_reset.html')

