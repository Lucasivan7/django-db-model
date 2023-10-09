# Generated by Django 4.2.6 on 2023-10-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField(max_length=40)),
                ('locacion', models.CharField(max_length=120)),
                ('observacion', models.CharField(max_length=250)),
                ('ruc_ci', models.IntegerField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('raza', models.TextField(blank=True, null=True)),
            ],
        ),
    ]