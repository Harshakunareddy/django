from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def Booklist(request):
    booksobj = Booksmodel.objects.all()
    serializer = Bookserializer(booksobj,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Booklist_post(request):
    booksobj = Booksmodel.objects.all()
    serializer = Bookserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def Booklist_update(request,id):
    booksobj = Booksmodel.objects.get(id=id)
    serializer = Bookserializer(instance=booksobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def Booklist_delete(request,id):
    booksobj = Booksmodel.objects.get(id=id)
    booksobj.delete()
    return Response("item deleted successfully")











