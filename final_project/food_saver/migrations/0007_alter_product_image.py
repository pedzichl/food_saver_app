# Generated by Django 3.2.4 on 2021-07-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_saver', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
