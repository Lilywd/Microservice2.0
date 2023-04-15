from rest_framework import serializers
from .models import ProductCommentModel

class ProductCommentsSerializer(serializers.ModelSerializer):
    comment = serializers.CharField()
    userID = serializers.IntegerField()
    productID = serializers.IntegerField()
    edited = serializers.BooleanField(required = False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = ProductCommentModel
        fields = ["comment", "userID", "productID", "edited", "created_at", "updated_at", "edited"]
