""" Sales models """

# Django
from django.db import models

# Models
from apps.productManagement.models import ManagementProduct
from apps.user.models import User

# Create your models here.
class Sale(models.Model):
    """ Sales model """
    sales_id = models.AutoField(primary_key=True)
    voucher_type = models.CharField(max_length=100, blank=False, null=False)    
    date = models.DateTimeField(auto_now=True, blank=False, null=False)
    tax = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)   
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,related_name='user' )
    products = models.ManyToManyField(ManagementProduct, through='Sale_detail', related_name='products') #

class Sale_detail(models.Model):
    """ Sales detail model """
    sales_detail_id = models.AutoField(primary_key=True)
    sales = models.ForeignKey(Sale, on_delete=models.CASCADE) #
    product = models.ForeignKey(ManagementProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
