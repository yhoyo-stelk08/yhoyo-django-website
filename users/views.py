from django.shortcuts import render
# import auth forms
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    ctx = {
        'title' : 'User Page',
    }
    return render(request,'users/index.html',ctx)

def register(request):
    form_user = UserCreationForm
    ctx = {
        'title' : 'Form Register User',
        'form_user' : form_user,
    }
    return render(request,'users/register.html',ctx)