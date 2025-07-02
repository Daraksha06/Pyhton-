from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=20)
    email = models.EmailField()
    phone=models.CharField(max_length=10)
    age=models.IntegerField()

    # now go to admin.py and register this model