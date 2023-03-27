from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .models import *
from .serializers import *

@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    s = StudentSerializer(student_obj,many=True)
    return Response({"status":200,'message':s.data})

@api_view()
def post(request):
    data=request.data
    print(data)
    return Response({'status':200,'payload':data})
