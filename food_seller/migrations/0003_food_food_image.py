# Generated by Django 3.2.19 on 2024-02-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_seller', '0002_food_food_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
