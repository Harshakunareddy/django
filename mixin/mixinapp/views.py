from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin


# Create your views here.


class studentlist(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    def get(self,request):
        return self.list(request)


class studentcreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    def post(self,request):
        return self.create(request)

class studentretrive(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)

class studentdestroy(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    def get(self,request,**kwargs):
        return self.destroy(request,**kwargs)

class studentupdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)