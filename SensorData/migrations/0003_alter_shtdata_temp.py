# Generated by Django 5.1 on 2024-08-25 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SensorData', '0002_bmpdata_devicedata_shtdata_remove_sensordata_payload_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shtdata',
            name='temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Temperatura'),
        ),
    ]
