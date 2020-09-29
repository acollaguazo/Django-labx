"""djangolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url 
from django.contrib import admin
from django.urls import path
from apirest import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/sensores$', views.sensor_data_list),
    url(r'^api/sensores/(?P<pk>[0-9]+)$', views.sensor_data_detail),
    url(r'^db/nuevo-jwt', obtain_jwt_token),    
    url(r'^auth-jwt-refresh', refresh_jwt_token),
    url(r'^auth-jwt-verify', verify_jwt_token),
]

