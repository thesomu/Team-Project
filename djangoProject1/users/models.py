from django.db import models


# Create your models here.
#================================================================================
#Customer(), Model which stores the details of Customer inserted from HTML form
#================================================================================

class Customer(models.Model):
    cust_fname = models.CharField(max_length=20)
    cust_lname = models.CharField(max_length=20)
    cust_uname = models.CharField(max_length=20)
    cust_password = models.CharField(max_length=20)
    cust_email = models.CharField(max_length=50)
    cust_phone = models.IntegerField()


#================================================================================
# Shipping(), Model which stores the details of Shipping insered from HTML form
#================================================================================

class Shipping(models.Model):
    ship_fname = models.CharField(max_length=20)
    ship_lname = models.CharField(max_length=20)
    ship_phone = models.CharField(max_length=10)
    ship_address = models.CharField(max_length=200)