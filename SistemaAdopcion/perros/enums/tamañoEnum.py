from django.db import models

class Tamaño(models.TextChoices):
    CHICO = 'chico', 'Chico'
    MEDIANO = 'mediano', 'Mediano'
    GRANDE = 'grande', 'Grande'
    GIGANTE = 'gigante', 'Gigante'
