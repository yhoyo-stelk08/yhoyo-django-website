"""djangoproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from . import views
from users import views as user_views

urlpatterns = [
    # admin path
    path('admin/', admin.site.urls),
    # food_seller app path
    path('food_seller/', include('food_seller.urls',namespace='food_seller')),
    # users app path
    path('users/', include('users.urls',namespace='users')),
    path('login/',user_views.user_login,name='login'),
    path('logout/',user_views.user_logout,name='logout'),
    # home index path
    path('',views.index,name='index'),
    
]
