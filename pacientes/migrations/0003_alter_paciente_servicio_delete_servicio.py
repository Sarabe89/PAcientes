# Generated by Django 4.2.3 on 2023-07-12 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_paciente_servicio_delete_pacientes_delete_servicios_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='servicio',
            field=models.CharField(choices=[('Polivalente', 'Polivalente'), ('Clinica Medica', 'Clinica Medica'), ('Guardia Adultos', 'Guarda de Adultos')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
    ]
