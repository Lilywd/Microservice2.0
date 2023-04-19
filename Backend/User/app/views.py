from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import User, UserUpdate
from .permissions import IsStaff, Admin
import requests
# Create your views here.

@api_view(["GET"])
def ping(request):
    message = {"reply": "ping"}
    return Response(message, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated, Admin])
def IsAdmin(request):
    return Response(status= status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def IsAuth(request):
    return Response(status= status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsStaff])
def IsStaff(request):
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated, Admin])
def addAdmin(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    user.is_staff = True
    user.is_admin = True
    user.save()
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated, Admin])
def removeAdmin(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    user.is_admin = False
    user.save()
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated, Admin])
def addStaff(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    user.is_staff = True
    user.save()
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated, Admin])
def removeStaff(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    user.is_admin = False
    user.is_staff = False
    user.save()
    return Response(status= status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated, Admin])
def deleteUser(request):
    email = request.data.get("email")
    user = get_object_or_404(User, email=email)
    id = user.id
    # url = f"http://localhost:8002/delete_all_user_comment/{id}"
    # requests.delete(url)
    user.delete()
    return Response(status= status.HTTP_200_OK)

class UpdateProfile(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdate
    def patch(self, request):
        user = request.user
        data = request.data
        serializer = self.serializer_class(data = data, instance = user, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status =status.HTTP_200_OK)
        return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def userDetails(request, pk):
    user = get_object_or_404(User, id = pk)
    data = {}
    data["name"] = user.first_name + " " + user.last_name
    data["pics"] = user.profile_picture.url
    return Response(data = data, status= status.HTTP_200_OK)