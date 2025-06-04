from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, default='disponible') 
    def __str__(self):
        return f"{self.nombre} ({self.raza})"

class UsuarioAdoptante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    preferencia_mascota = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Postulacion(models.Model):
    usuario = models.ForeignKey(UsuarioAdoptante, on_delete=models.CASCADE)
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    confirmada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario} - {self.perro}"
