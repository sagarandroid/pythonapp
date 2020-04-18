from django.shortcuts import render

from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import SignUp
from . serializer import SignUpSerializer
from rest_framework.decorators import api_view

# Create your views here.

class userlist(APIView):

    def get(self,request):
        countrieslist=SignUp.objects.all()
        serializer=SignUpSerializer(countrieslist,many=True)
        return Response(serializer.data)

    def post(self):
        pass


    
class login(APIView):

    def get(self,request,pk):
        countrieslist=SignUp.objects.get(id=pk)
        serializer=SignUpSerializer(countrieslist,many=False)
        return Response(serializer.data)

    def post(self):
        pass

 

    
    
class update(APIView):

    def get(self,request,pk):
        pass

    def post(self,request,pk):
        countrieslist=SignUp.objects.get(id=pk)
        serializer = SignUpSerializer(instance=countrieslist,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["sucess"]="updated"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



       

