from pyexpat import model
from re import L
from statistics import mode
from sys import api_version
from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobileNo = models.CharField(max_length=10)
    Address = models.TextField(max_length=100)
    password = models.CharField(max_length=15)
    createdOn = datetime.now()
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
    title = models.CharField(max_length=20)
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
        
        
class Discount(models.Model):
    discountName = models.CharField(max_length=20)
    discountValue= models.CharField(max_length=200)
    class Meta:
        db_table = 'Discount'
        
class Size(models.Model):
    sizeName = models.CharField(max_length=30)
    sizeValue = models.IntegerField()
    class Meta:
        db_table = 'Size'


class Color(models.Model):
    colorName = models.CharField(max_length=30)
    colorCode = models.CharField(max_length=30)
    class Meta:
        db_table = 'Color'

class Gender(models.Model):
    genderType = models.CharField(max_length=20)
    class Meta:
        db_table = 'Gender'
        
        
class Brand(models.Model):
    brandName = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    class Meta:
        db_table = 'Brand'

class Slider(models.Model):
    # image = models.fi
    heading = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    class Meta:
        db_table = 'Slider'

class Staff(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    mobileNo = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    adharNo = models.CharField(max_length=20)
    class Meta:
        db_table = '__all__'
        

       
        
class Cart(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    class Meta:
        db_table = 'Cart'
        
class Wishlist(models.Model):
        productId = models.ForeignKey(Product, on_delete=models.CASCADE)
        class Meta:
            db_table = 'Wishlist'




