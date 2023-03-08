"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from app5.views import *
from app6.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app5_first/',app5_first,name='app5_first'),
    path('app5_second/',app5_second,name='app5_second'),
    path('app6_first/',app6_first,name='app6_first'),
    path('app6_second/',app6_second,name='app6_second'),

]
