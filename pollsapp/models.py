from django.db import models

# Create your models here.

class Empleado(models.Model):
    pass
matricula = models.AutoField()
numerosocial = models.SmallIntegerField()
nip =  models.SmallIntegerField()
nombre = models.CharField(max_length = 150)
area = models.CharField(max_length = 150)
encuesta =  models.SmallIntegerField()


class Pregunta(models.Model):

    condiciones=models.IntegerField()
    cooperacion=models.IntegerField()
    supervision=models.IntegerField()
    condicionesfisicas=models.IntegerField()
    satisfaccion=models.IntegerField()
    participacion=models.IntegerField()