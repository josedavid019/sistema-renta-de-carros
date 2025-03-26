# Generated by Django 5.1.7 on 2025-03-26 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='descripcion_adicional',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fotos',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='historial_accidentes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='historial_mantenimientos',
            field=models.TextField(blank=True),
        ),
    ]
