from django.shortcuts import render
from django.http import HttpResponse
from .models import Food

# Create your views here.

# function for index of food_seller
def index(request) :
    food_list = Food.objects.all()
    ctx = {
        'title' : 'We sell food and beverages',
        'food_list' : food_list, 
    }
    print(food_list)
    return render(request,'food_seller/index.html',ctx)

# function for detail of food
def food_detail(request,name) :
    # get food based on food_name
    detail = Food.objects.get(food_name=name)
    print(detail)

    ctx = {
        'title' : 'Item Details',
        'detail' : detail,
    }
    return render(request, 'food_seller/detail.html', ctx)
    

