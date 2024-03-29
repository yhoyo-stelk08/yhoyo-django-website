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
# from users import views as user_views
from django.contrib.auth import views as auth_views
# setting for user uploaded files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin path
    path('admin/', admin.site.urls),
    # food_seller app path
    path('food_seller/', include('food_seller.urls',namespace='food_seller')),
    # users app path
    path('users/', include('users.urls',namespace='users')),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    # home index path
    path('',views.index,name='index'),
    
]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
