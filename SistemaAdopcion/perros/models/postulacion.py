from django.db import models
from .perro import Perro
from .usuario_adoptante import UsuarioAdoptante

class Postulacion(models.Model):
    usuario = models.ForeignKey(UsuarioAdoptante, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    confirmada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario} - {self.perro}"