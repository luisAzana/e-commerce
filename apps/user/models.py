""" Users models """

# Django
import imp
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    