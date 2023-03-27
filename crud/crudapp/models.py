from django.db import models

# Create your models here.
class Booksmodel(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    read_by = models.CharField(max_length=100)