from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import User
from .permissions import IsStaff, Admin
# Create your views here.

@api_view(["GET"])
def ping(request):
    message = {"reply": "ping"}
    return Response(message, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([Admin])
def IsAdmin(request):
    return Response(status= status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsStaff])
def IsStaff(request):
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([Admin])
def addAdmin(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    user.is_staff = True
    user.is_admin = True
    user.save()
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([Admin])
def removeAdmin(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    user.is_admin = False
    user.save()
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([Admin])
def addStaff(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    user.is_staff = True
    user.save()
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([Admin])
def removeStaff(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    user.is_admin = False
    user.is_staff = False
    user.save()
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([Admin])
def deleteUser(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    user.delete()
    return Response(status= status.HTTP_200_OK)