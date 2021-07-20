from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField
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

CATEGORIES = (
    (1, 'fruits and vegetables'),
    (2, 'processed food'),
    (3, 'sweets'),
    (4, 'liquids'),
    (5, 'meats'),
    (6, 'seafood'),
    (7, 'fish'),
    (8, 'juices'),
    (9, 'dry products'),
    (10, 'cleaning products')
     )

class Product(models.Model):
    name = models.CharField(max_length=128)
    expiration_date = models.DateField()
    quantity = models.IntegerField()
    unit = models.IntegerField(choices=UNITS_CHOICES)
    type = models.IntegerField(choices=DIET_TYPE)
    image = StdImageField(blank=True, null=True, upload_to='media', default='final_project/media/media/default_product.png', variations={'thumbnail': {'width': 100, 'height': 75}})
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return "{}{} {}".format(self.id, '.', self.name)


class ProductUser(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UsersSavedProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.IntegerField(choices=CATEGORIES)
    products = models.ManyToManyField(Product, through='ProductCategory')


class ProductCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    city = models.CharField(max_length=64, null=True)
    phone = models.IntegerField(null=True)