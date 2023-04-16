from django.urls import path
from . import views

urlpatterns = [
    path('', views.ping, name="ping"),
    path('product_comment', views.ProductCommentsCreate.as_view(), name="product_comments_create"),
    path('delete_all_comments/<str:pk>/', views.ProductCommentsDelete.as_view(), name="product_comments_deletes"),
    path('delete_all_user_comment/<str:pk>/', views.UserCommentsDelete.as_view(), name="user_comments_deletes"),
    path('single_product/<str:pk>', views.ProductComments.as_view(), name="single_product"),
    path('single_comment/<str:pk>/<str:ui>', views.UserProductComments.as_view(), name="delete_comment"),
]
