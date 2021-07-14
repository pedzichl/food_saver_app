# Generated by Django 3.2.4 on 2021-07-13 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_saver', '0004_particularuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductParticularUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_saver.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_saver.particularuser')),
            ],
        ),
        migrations.AddField(
            model_name='particularuser',
            name='products',
            field=models.ManyToManyField(through='food_saver.ProductParticularUser', to='food_saver.Product'),
        ),
    ]