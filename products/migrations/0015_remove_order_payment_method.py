# Generated by Django 4.1 on 2023-03-28 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_method',
        ),
    ]
