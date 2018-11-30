from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z]+')
# create your models here


class UserManager(models.Manager):
    def validation(self, postData):
        errors = {}
        if len(postData['user_name']) < 1:
            errors['user_name'] = "please enter your user name."
        elif len(postData['user_name'])<2:
            errors['user_name'] = "First name must be at least 2 characters."
        # elif not re.match(NAME_REGEX, postData['user_name']):
        #     errors['user_name'] = "user name may only contain letters."

        if len(postData['first_name']) < 1:
            errors['first_name'] = "please enter your first name."
        elif len(postData['first_name'])<2:
            errors['first_name'] = "First name must be at least 2 characters."
        elif not re.match(NAME_REGEX, postData['first_name']):
            errors['first_name'] = "First name may only contain letters."

        if len(postData['last_name']) < 1:
            errors['last_name'] = "please enter your last name."
        elif len(postData['last_name'])<2:
            errors['last_name'] = "Last name must be at least 2 characters."
        elif not re.match(NAME_REGEX, postData['last_name']):
            errors['last_name'] = "Last name may only contain letters."


        if len(postData['email']) < 1:
            errors['email'] = "Please enter your email."
        elif User.objects.filter(email=postData['email']):
            errors['email'] = "Email is already taken"
        elif not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "Incorrect email format."

        if len(postData['password']) < 1:
            errors['password'] = "Please enter a password."
        elif len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        

        return errors

    def login_validation(self, postData):
        print (postData)
        print ("========" + postData['loginmail'])
        print ("+++++++++" + postData['loginpass'])
        errors = {}
        if len(postData['loginmail']) < 1:
            #if the login email is empty, throw out an error "Please enter your email."
            errors['loginmail'] = "Please enter your email."
        elif not User.objects.filter(email=postData['loginmail']):
            errors['loginmail'] = "Incorrect email."
        elif len(postData['loginpass']) < 1:
            errors['loginpass'] = "Please enter your password."
        elif not bcrypt.checkpw(postData['loginpass'].encode(), User.objects.get(email=postData['loginmail']).password.encode()):
            errors['loginpass'] = "Incorrect password."
        return errors

        
class User(models.Model):
    user_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now_add = True)
    admin = models.BooleanField(default=True)
    objects = UserManager()

# class Role(models.Model)
    

