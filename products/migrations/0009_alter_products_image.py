# Generated by Django 4.1 on 2023-03-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='item-6.jpeg', upload_to=''),
        ),
    ]
