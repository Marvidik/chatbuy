# Generated by Django 4.1 on 2023-03-28 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_cart_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='store',
        ),
    ]
