from django.urls import path
from . import views

app_name='food_seller'

urlpatterns = [
    # index
    # class based view
    path('',views.FoodListView.as_view(),name='index'),
     # detail food
    path('<int:pk>',views.FoodDetailView.as_view(),name='food_detail'),
    # add food
    path('create/',views.FoodCreateView.as_view(),name='food_create'),
    # edit food
    path('edit/<int:pk>',views.FoodEditView.as_view(),name='food_edit'),
    # delete food
    path('delete/<int:pk>',views.FoodDeleteView.as_view(),name='food_delete'),

    # function based view
    # path('',views.index,name='index'),
    # detail food
    # path('<int:food_id>',views.food_detail,name='food_detail'),
    # add food
    # path('create/',views.food_create,name='food_create'),
    # edit food
    # path('edit/<int:food_id>',views.food_edit,name='food_edit'),
    # delete food
    # path('delete/<int:food_id>',views.food_delete,name='food_delete'),

    
]