# Generated by Django 3.0.8 on 2020-07-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200727_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='name',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
