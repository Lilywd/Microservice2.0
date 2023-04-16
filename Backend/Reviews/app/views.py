from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from .serializers import ProductCommentsSerializer
from .models import ProductCommentModel
import requests

# Create your views here.
@api_view(["GET"])
def ping(request):
    message = {"reply": "ping"}
    return Response(message, status=status.HTTP_200_OK)

class ProductCommentsCreate(generics.GenericAPIView):
    serializer_class = ProductCommentsSerializer
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status =status.HTTP_201_CREATED)
        return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ProductComments(generics.GenericAPIView):
    serializer_class = ProductCommentsSerializer
    queryset = ProductCommentModel.objects.all()
    def get(self, request, pk):
        products = ProductCommentModel.objects.filter(productID = pk)
        serializer = self.serializer_class(products, many = True)
        comments = []
        for data in serializer.data:
            url = "http://localhost:8002/user_details/{}".format(data['userID'])
            response = requests.get(url).json()
            data["name"] = response["name"]
            data["picture"] = response["pics"]
            comments.append(data)
        return Response(data = comments, status =status.HTTP_200_OK)


class UserProductComments(generics.GenericAPIView):
    serializer_class = ProductCommentsSerializer
    def patch(self, request, pk, ui):
        product = get_object_or_404(ProductCommentModel, productID = pk, userID = ui)
        data = request.data
        data['edited'] = "true"
        serializer = self.serializer_class(data = data, instance = product, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status = status.HTTP_200_OK)
        return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, ui):
        product = get_object_or_404(ProductCommentModel, productID = pk, userID = ui)
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class ProductCommentsDelete(generics.GenericAPIView):
    serializer_class = ProductCommentsSerializer
    queryset = ProductCommentModel.objects.all()
    def delete(self, request, pk):
        products = ProductCommentModel.objects.filter(productID = pk)
        for data in products:
            data.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)

class UserCommentsDelete(generics.GenericAPIView):
    serializer_class = ProductCommentsSerializer
    queryset = ProductCommentModel.objects.all()
    def delete(self, request, pk):
        products = ProductCommentModel.objects.filter(userID = pk)
        for data in products:
            data.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)