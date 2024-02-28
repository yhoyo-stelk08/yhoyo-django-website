from django import forms
from .models import Food

class FoodForm(forms.Form) :
    class Meta:
        model = Food
