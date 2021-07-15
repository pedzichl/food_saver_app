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
    location = models.CharField(max_length=128, default='')
    name = models.CharField(max_length=128)
    expiration_date = models.DateField()
    quantity = models.IntegerField()
    unit = models.IntegerField(choices=UNITS_CHOICES)
    type = models.IntegerField(choices=DIET_TYPE)
    image = models.ImageField(blank=True, null=True, upload_to='media')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return "{}{} {}".format(self.id, '.', self.name)


class ProductUser(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



