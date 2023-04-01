# Generated by Django 4.1 on 2023-03-28 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_alter_order_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartsorder', to='products.cart'),
        ),
    ]
