from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name