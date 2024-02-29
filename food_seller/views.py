from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Food
from .forms import FoodForm

# Create your views here.

# function for index of food_seller
def index(request) :
    food_list = Food.objects.all().order_by('id')
    ctx = {
        'title' : 'We sell food and beverages',
        'food_list' : food_list, 
    }
    # print(food_list)
    return render(request,'food_seller/index.html',ctx)

# function for detail of food
def food_detail(request,food_id) :
    # get food based on food id
    detail = Food.objects.get(id=food_id)
    # print(detail)

    ctx = {
        'title' : 'Item Details',
        'detail' : detail,
    }
    return render(request, 'food_seller/detail.html', ctx)
    
def food_create(request):
    form_data = FoodForm(request.POST or None)

    if form_data.is_valid() :
        form_data.save()

        return redirect('food_seller:index')
    
    ctx = {
        'title' : 'Add Food Form',
        'form' : form_data,
    }
    return render(request,'food_seller/food_form.html',ctx)

def food_edit(request,food_id):
    food = Food.objects.get(id=food_id)
    form_data = FoodForm(request.POST or None,instance=food)

    if form_data.is_valid() :
        form_data.save()
        return redirect('food_seller:index')
        # return render('food_seller/edit/'+str(food.id))

    ctx = {
        'title' : 'Food Edit Form',
        'form' : form_data,
        'food' : food,
    }

    return render(request,'food_seller/food_form.html',ctx)

def food_delete(request,food_id):
    food = Food.objects.get(id=food_id)

    if request.method == "POST":
        food.delete()
        return redirect('food_seller:index')
    
    ctx = {
        'title' : 'Food Delete Form',
        'food' : food,
    }

    return render(request,'food_seller/food_delete.html',ctx)