# Generated by Django 4.1 on 2023-03-27 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_vendor_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.vendor')),
            ],
        ),
    ]