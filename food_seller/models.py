from django.db import models

# Create your models here.

class Food(models.Model) :

    food_name = models.CharField(max_length=50,null=False)
    food_desc = models.TextField()
    food_price = models.FloatField(default=0,null=False)
    food_stock = models.IntegerField(default=0,null=False)

    def __str(self) :
        return "{}. {}".format(self.id,self.food_name)