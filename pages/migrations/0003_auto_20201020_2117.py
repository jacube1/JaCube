# Generated by Django 3.1.2 on 2020-10-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
