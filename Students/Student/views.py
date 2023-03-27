from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset = Bookmodels.objects.all()
    seri = BookSerializer