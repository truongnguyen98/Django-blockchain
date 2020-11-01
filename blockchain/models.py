from django.db import models
from hashlib import sha256
import datetime
import logging
import pytz
from django.urls import reverse


class Transaction (models.Model):
    index = models.IntegerField(auto_created=True, blank=True,null=True)
    product_id = models.IntegerField()
    current_date = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(blank=True,null=True)
    country = models.CharField(max_length=50)
    amount = models.IntegerField()
    common_name= models.TextField(blank=True, max_length=255,null=True)
    #fileAttached = models.FileField()
    

    def __str__(self):
        return "Transaction " + str(self.index)

class ProducerModel(models.Model):
    index = models.IntegerField(auto_created=True, blank=True,null=True)
    product_id = models.IntegerField()
    current_date = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(blank=True,null=True)
    country = models.CharField(max_length=50)
    amount = models.IntegerField()
    common_name= models.TextField(blank=True, max_length=255,null=True)


class ShipperModel(models.Model):
    index = models.IntegerField(auto_created=True, blank=True,null=True)
    product_id = models.IntegerField()
    current_date = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(blank=True,null=True)
    country = models.CharField(max_length=50)
    amount = models.IntegerField()
    common_name= models.TextField(blank=True, max_length=255,null=True)

   
class WholesalerModel(models.Model):
    index = models.IntegerField(auto_created=True, blank=True,null=True)
    product_id = models.IntegerField()
    current_date = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(blank=True,null=True)
    country = models.CharField(max_length=50)
    amount = models.IntegerField()
    common_name= models.TextField(blank=True, max_length=255,null=True)


class DetailerModel(models.Model):
    index = models.IntegerField(auto_created=True, blank=True,null=True)
    product_id = models.IntegerField()
    current_date = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(blank=True,null=True)
    country = models.CharField(max_length=50)
    amount = models.IntegerField()
    common_name= models.TextField(blank=True, max_length=255,null=True)
