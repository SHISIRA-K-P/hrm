from email.policy import HTTP
import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer,LoginSerializer
from .models import User 
from django.contrib.auth import authenticate,login
from rest_framework import authentication,permissions


class UserView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        user_obj=User.objects.all()
        serializer=UserSerializer(user_obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        user_obj=User.objects.get(id=id)
        serializer=UserSerializer(user_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        patient_obj=User.objects.get(id=id)
        serializer=UserSerializer(instance=patient_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.error_messages)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        user_obj=User.objects.get(id=id)
        user_obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_200_OK)




class SignInView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            uname=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user=authenticate(request,username=uname,password=password)
            print(user)
            if user:
                login(request,user)
                return Response({"msg":"success"})
            else:
                return Response({"msg":"Invalid credetials"})