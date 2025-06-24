from django.db import models
from ..enums.razaEnum import RazaPerro
from ..enums.estadoSaludEnum import EstadoSalud
from ..enums.edadEnum import Edad
from ..enums.tamañoEnum import Tamaño

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(
        max_length=20,
        choices=RazaPerro.choices,
        default=RazaPerro.OTRO
    )
    edad =  models.CharField(
        max_length=20,
        choices=Edad.choices,
        default=Edad.CACHORRO
    )
    tamaño =  models.CharField(
        max_length=20,
        choices=Tamaño.choices,
        default=Tamaño.CHICO
    )
    peso = models.FloatField(default=0)
    estado_salud =  models.CharField(
        max_length=20,
        choices=EstadoSalud.choices,
        default=EstadoSalud.SALUDABLE
    )
    vacunado = models.BooleanField(default=False)

    ESTADO_ADOPCION_CHOICES = [
        ('1', 'Disponible'),
        ('2', 'Adoptado'),
    ]

    estado_adopcion = models.CharField(
        max_length=20,
        choices=ESTADO_ADOPCION_CHOICES,
        default='disponible'
    )

    def __str__(self):
        return f"{self.nombre} ({self.raza})"