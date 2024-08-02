from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default='default@gmail.com')
    age = models.IntegerField(default=18)
    password = models.CharField(default='default@123',max_length=50)              