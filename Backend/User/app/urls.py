from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ping, name="ping"),
    path("isAuth", views.IsAuth, name="is-auth"),
    path("isAdmin", views.IsAdmin, name="is-admin"),
    path("isStaff", views.IsStaff, name="is-staff"),
    path("deleteUser", views.deleteUser, name="delete-user"),
    path("addAdmin", views.addAdmin, name="add-admin"),
    path("removeAdmin", views.removeAdmin, name="remove-admin"),
    path("addStaff", views.addStaff, name="add-staff"),
    path("removeStaff", views.removeStaff, name="remove-staff"),
    path("update_profile", views.UpdateProfile.as_view(), name= "update_profile"),
    path("user_details/<str:pk>", views.userDetails, name= "user_details")
]
