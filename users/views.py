from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {
        'title' : 'User Page',
    }
    return render(request,'users/index.html',ctx)