from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="User Microservice",
      default_version='v1',
      description="This documentation shows all the endpoints available for the user Microservice",
      terms_of_service="https://www.me.popsicool.tech",
      contact=openapi.Contact(email="akinolasamson1234@gmail.com"),
      license=openapi.License(name="Lilian Wanjiku"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('app.urls')),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.jwt")),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
