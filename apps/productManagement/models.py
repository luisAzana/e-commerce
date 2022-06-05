""" Product management model """

# Django
from contextlib import nullcontext
from distutils.command.upload import upload
from random import choices
from unicodedata import category
from django.db import models

# Create your models here.
class ManagementProduct(models.Model):
    product_id = models.CharField(primary_key=True, max_length=30,unique=True, blank=False)
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=60, blank=False)
    description = models.TextField(blank=True, max_length=250, null=True)
    price = models.IntegerField(blank=False)
    stock = models.IntegerField(blank=False)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    
    def __str__(self):
        return self.name
        