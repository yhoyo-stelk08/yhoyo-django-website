# Generated by Django 3.2.19 on 2024-02-27 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('food_desc', models.TextField()),
                ('food_price', models.FloatField(default=0)),
                ('food_stock', models.IntegerField(default=0)),
            ],
        ),
    ]
