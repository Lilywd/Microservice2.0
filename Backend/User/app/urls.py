from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ping, name="ping"),
    path("isAdmin", views.IsAdmin, name="is-admin"),
    path("isStaff", views.IsStaff, name="is-staff"),
    path("addAdmin", views.addAdmin, name="add-admin"),
    path("removeAdmin", views.removeAdmin, name="remove-admin"),
    path("addStaff", views.addStaff, name="add-staff"),
    path("removeStaff", views.removeStaff, name="remove-staff"),
]
