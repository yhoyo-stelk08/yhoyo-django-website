from django import forms
from .models import Food

class FoodForm(forms.ModelForm) :
    class Meta:
        model = Food
        fields = ["food_name","food_desc","food_price","food_stock","food_category","food_image"]
