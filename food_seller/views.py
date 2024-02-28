from django.shortcuts import render
# from django.http import HttpResponse
from .models import Food

# Create your views here.
def index(request) :
    food_list = Food.objects.all()
    ctx = {
        'title' : 'We sell food and beverages',
        'food_list' : food_list,
    }
    return render(request,'food_seller/index.html',ctx)


def food_detail(request,food_name) :
    food_detail = Food.objects.get(food_name=food_name)
    print(food_detail)

    ctx = {
        'title' : 'Item Details',
    }
    return render(request,'food_seller/detail.html',ctx)

