# Generated by Django 3.1.2 on 2020-10-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_product_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='amount',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
