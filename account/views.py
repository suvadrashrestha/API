from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import  UserRegistrationSerializer,UserLoginSerializer
from django.contrib.auth import authenticate

class UserRegistrationView(APIView):
    def post(self,request,format=None):
      #sets the data attribute with request.value 
      serializer=UserRegistrationSerializer(data=request.data)
      #check if any field is empty, runs validate() and set validate_data with user data
      if serializer.is_valid(raise_exception=True):
         #returns the __str__ method of user model and .save() triggers the create method
         user=serializer.save()
        # print(user)
        #  return Response({"data":serializer.validated_data})
         return Response({"msg":" User registration view"},status=status.HTTP_201_CREATED)
      return Response(serializer,status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
   def post(self,request,format=None):
      serializer=UserLoginSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
         email=serializer.data.get("email")
         password=serializer.data.get("password")
         user=authenticate(email=email,password=password)
         if user is not None:
            return Response({"msg":"login success"},status=status.HTTP_200_OK)
         else:
            return Response({"errors":{'non_fields_errors':["email or password is not valid"]}},status=status.HTTP_404_NOT_FOUND)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)