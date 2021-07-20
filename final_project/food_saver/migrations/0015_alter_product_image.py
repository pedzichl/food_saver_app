# Generated by Django 3.2.5 on 2021-07-15 18:34

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('food_saver', '0014_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=stdimage.models.StdImageField(blank=True, default='food_saver/media/default_product.png', null=True, upload_to='media'),
        ),
    ]
