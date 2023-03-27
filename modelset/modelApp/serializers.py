from .models import *
from rest_framework import serializers

class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'