from .models import *
from rest_framework import serializers
class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Booksmodel
        fields = '__all__'
