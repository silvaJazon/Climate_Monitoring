# Generated by Django 5.1 on 2024-08-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SensorData', '0003_alter_shtdata_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmpdata',
            name='press',
            field=models.FloatField(blank=True, null=True, verbose_name='Pressao'),
        ),
        migrations.AlterField(
            model_name='bmpdata',
            name='temp',
            field=models.FloatField(blank=True, null=True, verbose_name='Temperatura'),
        ),
        migrations.AlterField(
            model_name='shtdata',
            name='a_temp',
            field=models.BooleanField(blank=True, null=True, verbose_name='Alarme de Temperatura'),
        ),
        migrations.AlterField(
            model_name='shtdata',
            name='a_umid',
            field=models.BooleanField(blank=True, null=True, verbose_name='Alarme de Umidade'),
        ),
        migrations.AlterField(
            model_name='shtdata',
            name='umid',
            field=models.FloatField(blank=True, null=True, verbose_name='Umidade'),
        ),
    ]
