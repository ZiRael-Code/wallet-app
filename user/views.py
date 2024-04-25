from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .exception.Invalid_details import InvalidDetailsException
from .services.user_servcie import UserServiceImp

# Create your views here.
users = UserServiceImp()


class register(APIView):
    def post(self, request):
        try:
            result = users.register(request)
            return Response(result, status=status.HTTP_200_OK)
        except InvalidDetailsException:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class login(GenericAPIView):
    def post(self, request):
        response = users.login(request)
        return Response(response, status=status.HTTP_200_OK)
