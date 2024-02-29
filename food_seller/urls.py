from django.urls import path
from . import views

app_name='food_seller'

urlpatterns = [
    path('',views.index,name='index'),
    # detail food
    path('<int:food_id>',views.food_detail,name='food_detail'),
    # add food
    path('create/',views.food_create,name='food_create'),
    # edit food
    path('edit/<int:food_id>',views.food_edit,name='food_edit'),
    # delete food
    path('delete/<int:food_id>',views.food_delete,name='food_delete'),
]