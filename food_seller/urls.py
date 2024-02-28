from django.urls import path
from . import views

app_name='food_seller'

urlpatterns = [
    path('',views.index,name='index'),
    # detail food
    # path()
    path('<str:name>',views.food_detail,name='food_detail')
]