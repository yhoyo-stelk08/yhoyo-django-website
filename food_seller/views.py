from django.shortcuts import render

# Create your views here.
def index(request) :
    ctx = {
        'title' : 'We sell food and beverages'
    }
    return render(request,'food_seller/index.html',ctx)