from django.db import models
from datetime import datetime
# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
def __str__(self):
    return self.name