# Generated by Django 3.0.8 on 2020-07-27 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200727_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
