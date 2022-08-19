import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from hrmapp.models import Leave, Feedback
from hrmapp.serializers import LeaveSerializer, FeedbackSerializer
from authentication.models import User 
from django.contrib.auth import authenticate, login
from rest_framework import authentication, permissions
import logging as log


class LeaveView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        try:
            leave_obj = Leave. objects.all()
            log.info("Retrieve  all object")
            serializer = LeaveSerializer(leave_obj, many=True)
            log.info("serializing data")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print("\nException Occured", error)

    def post(self, request, *args, **kwargs):
        serializer = LeaveSerializer(data=request.data)
        log.info("serializing data")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
            
            
class LeaveDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            leave_obj = Leave.objects.get(id=id)
            log.info("Retrieve  an object with specific id")
            serializer = LeaveSerializer(leave_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print("\nException Occured", error)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        leave_obj = Leave.objects.get(id=id)
        serializer = LeaveSerializer(leave_obj, data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            leave_obj = Leave.objects.get(id=id)
            leave_obj.delete()
            log.info("object deleted")
            return Response({"msg": "deleted"}, status=status.HTTP_200_OK)
        except Exception as error:
            print("\nException Occured", error)


class FeedbackView(APIView):
    permission_classes = [permissions.IsAuthenticated]
  
    def get(self, request, *args, **kwargs):
        try:
            feedback_obj = Feedback.objects.all()
            serializer = FeedbackSerializer(feedback_obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print("\nException Occured", error)

    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class FeedbackDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            feedback_obj = Feedback.objects.get(id=id)
            serializer = FeedbackSerializer(feedback_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print("\nException Occured", error)

    def put(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            feedback_obj = Feedback.objects.get(id=id)
            serializer = FeedbackSerializer(instance=feedback_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors)
        except Exception as error:
            print("\nException Occured", error)

    def delete(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            feedback_obj = Feedback.objects.get(id=id)
            feedback_obj.delete()
            return Response({"msg": "deleted"}, status=status.HTTP_200_OK)
        except Exception as error:
            print("\nException Occured", error)


class StatusUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            user_obj = User.objects.get(id=id)
            leave_obj = Leave.objects.get(user=user_obj)
            serializer = LeaveSerializer(leave_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print("\nException Occured", error)
    
    def put(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            user_obj = User.objects.get(id=id) 
            if user_obj.is_superuser:
                    leave_obj = Leave.objects.get(user=user_obj)
                    serializer = LeaveSerializer(instance=leave_obj, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(serializer.errors)
            else:
                return Response({"msg": "user isn't superuser"})
        except Exception as error:
            print("\nException Occured", error)
