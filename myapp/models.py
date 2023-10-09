from django.db import models
import json




# Create your models here.
class Clientes(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    locacion = models.CharField(max_length=120)
    observacion = models.CharField(max_length=250)
    ruc_ci = models.IntegerField()

class Pacientes(models.Model):
     nombre = models.CharField(max_length=100)
     raza = models.TextField(default='Sharpei')
     pelaje = models.CharField(max_length=50, default='Peludo')
     nacimiento = models.DateField(null=True)
     peso = models.FloatField(default=None)
     especie = models.CharField(max_length=150, default='Perro')
     caracter = models.CharField(max_length=100, default='Maquiavelico')
     sexo = models.BooleanField(default=True)
     servicios = models.CharField(max_length=300, default='Atencion Clinica')
     observacion = models.TextField(default='Sin observaciones')

class Ficha_clinica(models.Model):
    alergias = models.CharField(max_length=120)
    antecedentes = models.CharField(max_length=250)
    sintomas_clinicos = models.CharField(max_length=150)
    piel_y_mucosa = models.CharField(max_length=100)
    temperatura_historica = models.FloatField()
    frecuencia_cardiaca = models.IntegerField()
    respiracion = models.CharField(max_length=100)
    dieta_tipo = models.CharField(max_length=100)
    medio_ambiente = models.CharField(max_length=100)
    medicamentos = models.CharField(max_length=100)
    otras_mascotas = models.CharField(max_length=150)
    fecha = models.DateField()





# raza_lista = ['Sharpei', 'Doberman', 'Pastor Aleman']
# raza_lista_json = json.dumps(raza_lista)
# instancia_raza = Pacientes(raza_json=raza_lista_json)
# instancia_raza.save()