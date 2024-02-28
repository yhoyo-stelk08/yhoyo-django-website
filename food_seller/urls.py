from django.urls import path
from . import views

app_name='food_seller'

urlpatterns = [
    path('',views.index,name='index'),
    # detail food
    path('<str:name>',views.food_detail,name='food_detail'),
    # add food
    path('create/',views.food_create,name='food_create'),
    # edit food
    path('edit/<int:id>',views.food_edit,name='food_edit')
    # delete food
]