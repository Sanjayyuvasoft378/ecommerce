from pyexpat import model
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

