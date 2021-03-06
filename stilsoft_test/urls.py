"""stilsoft_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from rest_framework import routers
from students.views import *

router = routers.SimpleRouter()
router.register(r'sections', SectionViewSet, basename='section')
router.register(r'memberships', MembershipViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/students/', StudentAPIList.as_view()),
    path('api/v1/students/<int:pk>/', StudentAPIUpdate.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include(router.urls)),
]
