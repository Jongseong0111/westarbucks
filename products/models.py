from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'menus'
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, default='')

    class Meta:
        db_table = 'categories'
    def __str__(self):
        return self.name

class Product(models.Model):
    korean_name  = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
    description  = models.TextField(default='')
    
    class Meta:
        db_table = 'products'
    def __str__(self):
        return self.korean_name


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    sodium           = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    saturated_fat    = models.DecimalField(max_digits=5, decimal_places=1, default =0)
    sugar            = models.DecimalField(max_digits=5, decimal_places=1, default =0)
    protein          = models.DecimalField(max_digits=5, decimal_places=1, default =0)
    caffeine         = models.DecimalField(max_digits=5, decimal_places=1, default =0)
    sodium           = models.DecimalField(max_digits=5, decimal_places=1, default =0)
    size_ml          = models.IntegerField(default=0)
    size_oz          = models.IntegerField(default=0)
    product          = models.ForeignKey('Product', on_delete=models.CASCADE, default='')

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    url = models.URLField(default='')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, default='')

    class Meta:
        db_table = 'images'

class Allergy(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'allergies'
    def __str__(self):
        return self.name

class Allergyproduct(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE,default='')
    product = models.ForeignKey('Product', on_delete=models.CASCADE,default='')


    class Meta:
        db_table = 'allergyproducts'


