# Generated by Django 3.2.5 on 2021-07-18 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_saver', '0029_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_saver.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_saver.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='products',
        ),
        migrations.DeleteModel(
            name='ProductRecipe',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(through='food_saver.ProductCategory', to='food_saver.Product'),
        ),
    ]
