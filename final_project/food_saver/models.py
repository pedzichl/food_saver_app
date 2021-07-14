from django.db import models
from django.contrib.auth.models import User
# Create your models here.
DIET_TYPE = (
    (1, 'no specific diet'),
    (2, 'vegetarian'),
    (3, 'vegan'),

)

UNITS_CHOICES = (
        (1, 'Kilogram'),
        (2, 'Gram'),
        (3, 'Liter'),
        (4, 'Mililiter'),
        (5, 'Pieces'),
    )


class Product(models.Model):
    name = models.CharField(max_length=128)
    expiration_date = models.DateField()
    quantity = models.FloatField()
    unit = models.IntegerField(choices=UNITS_CHOICES)
    type = models.IntegerField(choices=DIET_TYPE)
    image = models.ImageField(blank=True, null=True, upload_to='media/%Y%m&D/')
    def __str__(self):
        return "{}{} {}".format(self.id, '.', self.name)



class ExchangeProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_free = models.BooleanField()

class ParticularUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through="ProductParticularUser")

class ProductParticularUser(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(ParticularUser, on_delete=models.CASCADE)



