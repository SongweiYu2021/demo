from django.db import models
# from login.models import User
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=16, default='', blank=True)
    phone = models.CharField(max_length=16, default='', blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')



