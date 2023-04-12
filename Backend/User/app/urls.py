from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ping, name="ping"),
    path("isAdmin", views.IsAdmin, name="ping"),
]
