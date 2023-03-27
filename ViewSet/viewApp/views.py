from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class StudentViewSets(viewsets.ViewSet):
    def list(self,request):
        queryset = StudentModel.objects.all()
        serializer = StudentSerializers(queryset,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            queryset = StudentModel.objects.get(pk=id)
            serializer = StudentSerializers(queryset,many=True)
            return Response(serializer.data)

    def update(self,request,pk):
        id=pk
        queryset = StudentModel.objects.get(pk=id)
        serializer = StudentSerializers(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"complete data is updated"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_request)

    def destroy(self,request):
        queryset = StudentModel.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':"deleted"})

    def create(self,request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data created'})
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

