# Generated by Django 3.2.5 on 2021-07-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_saver', '0030_auto_20210718_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
