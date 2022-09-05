from pyexpat import model
from re import L
from statistics import mode
from sys import api_version
from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobileNo = models.CharField(max_length=10)
    Address = models.TextField(max_length=100)
    password = models.CharField(max_length=15)
    class Meta:
        db_table = 'User'
        
class mainCategory(models.Model):
    # slug = models.SlugField(unique=True, null=True)
    categoryName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    # image = models
    class Meta:
        db_table = 'MainCategory'
        
class SubCategory(models.Model):
    # slug = models.SlugField(unique=True, null=True)
    mainCategoryId = models.ForeignKey(mainCategory,on_delete=models.CASCADE)
    subCategoryName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    class Meta:
        db_table = 'SubCategory'
        
        
class Product(models.Model):
    # slug = models.SlugField(unique=True, null=True)
    mainCategoryId = models.ForeignKey(mainCategory,on_delete=models.CASCADE)
    SubCategoryId = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    productName = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    qty = models.PositiveIntegerField()
    class Meta:
        db_table = 'Product'
        
        
class Offer(models.Model):
    offerName = models.CharField(max_length=20)
    ofervalue = models.IntegerField()
    class Meta:
        db_table = 'Offer'
        



