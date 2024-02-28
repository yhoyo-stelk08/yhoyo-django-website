from django.db import models

# Create your models here.

class Food(models.Model) :
    # FOOD_CATEGORY = ('Food','Drink')
    food_name = models.CharField(max_length=50,null=False,unique=True)
    food_desc = models.TextField()
    food_price = models.FloatField(default=0,null=False)
    food_stock = models.IntegerField(default=0,null=False)
    food_category = models.TextChoices('Food','Drink')
    food_image = models.CharField(max_length=255,blank=True,default="",null=True)

    def __str__(self) :
        return "{}".format(self.food_name)