# Generated by Django 3.2.5 on 2021-07-17 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210717_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='caffeine',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='one_serving_kcal',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='product',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='protein',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='saturated_fat',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='sodium',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='sugar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]