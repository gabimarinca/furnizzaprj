from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True) 

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', "bio"]

    def __str__(self):
        return self.username
    #desc = models.TextField() 