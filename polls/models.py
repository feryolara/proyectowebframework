from django.db import models

# Create your models here.

class Empleado(models.Model):
matricula = models.AutoField(primary_key = True)
numerosocial = models.SmallIntegerField(null=True)
nip =  models.SmallIntegerField(null=True)
nombre = models.Charfield(max_length = 150)
area = models.Charfield(max_length = 150)
encuesta =  models.SmallIntegerField(null=True)
