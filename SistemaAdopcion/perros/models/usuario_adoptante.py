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

    def registrarse(self):
        print(f"Usuario registrado: {self.nombre} {self.apellido}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")

    def modificar_datos(self, nombre=None, apellido=None, email=None, telefono=None, direccion=None, pref_raza=None, pref_edad=None, pref_tamaño=None, pref_estado_salud=None):
        if nombre: self.nombre = nombre
        if apellido: self.apellido = apellido
        if email: self.email = email
        if telefono: self.telefono = telefono
        if direccion: self.direccion = direccion
        if pref_raza: self.pref_raza = pref_raza
        if pref_edad: self.pref_edad = pref_edad
        if pref_tamaño: self.pref_tamaño = pref_tamaño
        if pref_estado_salud: self.pref_estado_salud = pref_estado_salud

    def adoptar_perro(self, perro):
        self.perro_adoptado = perro
        self.historial_adopciones.append(perro)
        print(f"El usuario {self.nombre} ha adoptado a perro {perro.nombre}")

    def ver_historial(self):
        if not self.historial_adopciones:
            print("No hay historial de adopciones.")
        else:
            print("Historial de adopciones:")
            for perro in self.historial_adopciones:
                print(f"- {perro.nombre}")
