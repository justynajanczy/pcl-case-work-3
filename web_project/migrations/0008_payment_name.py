# Generated by Django 4.2 on 2023-05-01 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_project', '0007_remove_food_test_remove_fruit_test_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
