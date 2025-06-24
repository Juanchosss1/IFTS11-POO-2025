from django.db import models
from django.contrib.auth.models import User
from ..enums.estadoSaludEnum import EstadoSalud
from ..enums.edadEnum import Edad
from ..enums.tamañoEnum import Tamaño
from ..enums.razaEnum import RazaPerro


class UsuarioAdoptante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    pref_raza =  models.CharField(
        max_length=20,
        choices=RazaPerro.choices,
        default=RazaPerro.OTRO
    )
    pref_edad =  models.CharField(
        max_length=20,
        choices=Edad.choices,
        default=Edad.CACHORRO
    )
    pref_tamaño = models.CharField(
        max_length=20,
        choices=Tamaño.choices,
        default=Tamaño.CHICO
    )
    pref_estado_salud =  models.CharField(
        max_length=20,
        choices=EstadoSalud.choices,
        default=EstadoSalud.SALUDABLE
    )  