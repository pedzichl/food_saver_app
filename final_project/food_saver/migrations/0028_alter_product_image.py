# Generated by Django 3.2.5 on 2021-07-18 16:31

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('food_saver', '0027_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=stdimage.models.StdImageField(blank=True, default='final_project/media/default_product.png', null=True, upload_to='media'),
        ),
    ]
