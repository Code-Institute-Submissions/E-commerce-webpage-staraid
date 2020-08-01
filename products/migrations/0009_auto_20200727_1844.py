# Generated by Django 3.0.8 on 2020-07-27 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200727_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='specifications_environmental_operating_humidity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_environmental_operating_temperature',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_environmental_storage_humidity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_environmental_storage_temperature',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_mechanical_diameter',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_mechanical_length',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_mechanical_weight',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_powerconnectivity_consumption',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_powerconnectivity_input',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_powerconnectivity_supply',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_powerconnectivity_telescope',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_powerconnectivity_usb',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_sensor',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_sensor_peak',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_sensor_pixel',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_sensor_read_noise',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_sensor_resolution',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specifications_sensor_size',
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('value', models.CharField(max_length=254)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='products.Product')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]