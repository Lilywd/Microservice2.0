from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def ping(request):
    message = {"reply": "ping"}
    return Response(message)

@api_view(["GET"])
def IsAdmin(request):
    request.headers.get('User-Agent')
    print(request.Request)
    if request.user.groups.filter(name='Admin').exists():
        return Response(status= status.HTTP_200_OK)
    return Response(status=status.HTTP_403_FORBIDDEN)