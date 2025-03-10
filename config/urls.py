"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from config.routers import router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from main import urls

# Swagger dokumentatsiyasini sozlash
schema_view = get_schema_view(
    openapi.Info(
        title="Lesson 1",
        default_version='v1',
        description="To have a ready to the first lesson",
        terms_of_service="www.fintechhub.uz",
        contact=openapi.Contact(email="fintechhub@gmail.com"),
        license=openapi.License(name="fintechhub"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Account (fayl URLlaridan import)
    path('account/', include(urls)),

    # API view-set uchun
    path('view-set/', include(router.urls)),

    # Swagger UI va API sxemasi
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
