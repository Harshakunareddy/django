from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
