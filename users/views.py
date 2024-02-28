from django.shortcuts import render,redirect
# import auth forms
from django.contrib.auth.forms import UserCreationForm
# import messages function
from django.contrib import messages

def index(request):
    ctx = {
        'title' : 'User Page',
    }
    return render(request,'users/index.html',ctx)

def register(request):
    if request.method == "POST" :
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid() :
            username = form_user.cleaned_data.get('username')
            messages.success(request,f'Welcome {username} , your account has been created')
            return redirect('users:index')
    else :
        form_user = UserCreationForm()
    
    ctx = {
        'title' : 'Form Register User',
        'form_user' : form_user,
    }
    return render(request,'users/register.html',ctx)