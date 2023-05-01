# Generated by Django 4.2 on 2023-05-01 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_project', '0006_remove_drink_size_remove_drink_type_remove_food_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='test',
        ),
        migrations.RemoveField(
            model_name='fruit',
            name='test',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AddField(
            model_name='drink',
            name='size',
            field=models.CharField(choices=[('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='drink',
            name='type',
            field=models.CharField(choices=[('Coffee', 'Coffee'), ('Tea', 'Tea'), ('Juice', 'Juice')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='type',
            field=models.CharField(choices=[('B', 'BREAKFAST'), ('L', 'LUNCH'), ('D', 'DINNER')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fruit',
            name='type',
            field=models.CharField(default='Fruit', max_length=200, null=True),
        ),
    ]
