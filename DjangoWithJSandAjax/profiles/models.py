from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars', default='avatar.png')
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Profile of the user {self.user.username}'