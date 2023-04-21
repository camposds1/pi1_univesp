from django.db import models

class Paciente(models.Model):

    nome = models.CharField(
        max_length = 255,
        null = False,
        blank = False
    )

    sobrenome = models.CharField(
        max_length = 255,
        null = False,
        blank = False
    )

    sexo = models.CharField(
        max_length = 1,
        null = False,
        blank = False
    )

    data_nascimento = models.DateField(
        null = False,
        blank = False
    )

    cidade = models.CharField(
        max_length = 50,
        null = False,
        blank = False
    )

    estado = models.CharField(
        max_length = 2,
        null = False,
        blank = False
    )

    objetos = models.Manager()