from django.urls import path
from . import views

urlpatterns = [
    path('', views.ping, name="ping"),
    path('product_comments', views.ProductCommentsCreate.as_view(), name="product_comments"),
    path('single_comment/<str:pk>', views.ProductComments.as_view(), name="single_comment"),
    path('single_comment/<str:pk>/<str:ui>', views.ProductCommentsSingle.as_view(), name="delete_comment"),
]
