from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False) 
    last_name = models.CharField(max_length=50, blank=True)
    avatar_img = models.ImageField(default='')
    email = models.EmailField(blank=False, max_length=50)
