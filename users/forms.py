from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# make form class extends UserCreationForm to add custom fields into the form 
class RegisterUserForm(UserCreationForm) :
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']