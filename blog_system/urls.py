"""
URL configuration for blog_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import permissions, routers
from blog_system.swagger import schema_view

BASE_URL = 'blog/'
router = routers.DefaultRouter()

urlpatterns = [
    path(f'{BASE_URL}admin/', admin.site.urls),
    path(f'{BASE_URL}', include(router.urls)),  # Your API endpoints
    path(f'{BASE_URL}swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(f'{BASE_URL}redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
