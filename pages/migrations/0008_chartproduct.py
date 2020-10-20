# Generated by Django 3.1.2 on 2020-10-20 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20201020_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.product')),
            ],
        ),
    ]
