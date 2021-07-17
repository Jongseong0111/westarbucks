# Generated by Django 3.2.5 on 2021-07-17 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'allergies',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_name', models.CharField(max_length=100)),
                ('english_name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=1, max_digits=5)),
                ('saturated_fat', models.DecimalField(decimal_places=1, max_digits=5)),
                ('sugar', models.DecimalField(decimal_places=1, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=1, max_digits=5)),
                ('caffeine', models.DecimalField(decimal_places=1, max_digits=5)),
                ('sodium', models.DecimalField(decimal_places=1, max_digits=5)),
                ('size_ml', models.IntegerField(default=0)),
                ('size_oz', models.IntegerField(default=0)),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
        migrations.CreateModel(
            name='Allergyproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'allergyproducts',
            },
        ),
    ]
