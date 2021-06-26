from django.db import models

# Create your models here.
DIET_TYPE = (
    (1, 'no specific diet'),
    (2, 'vegetarian'),
    (3, 'vegan'),

)

class ParticularUser(models.Model):
    login = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    city_name = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    mail = models.EmailField(max_length = 254)
    created = models.DateField(auto_now_add=True)

class ProfessionalUser(models.Model):
    login = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    city_name = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    mail = models.EmailField(max_length = 254)
    created = models.DateField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=128)
    expiration_date = models.DateField()
    quantity = models.IntegerField()
    type = models.FloatField(choices=DIET_TYPE)

class DiscountedProducts(models.Model):
    products = models.ManyToManyField(Product)

class FreeExchangeProducts(models.Model):
    products = models.ManyToManyField(Product)