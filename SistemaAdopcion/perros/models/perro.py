from django.db import models
from ..enums.razaEnum import RazaPerro
from ..enums.estadoSaludEnum import EstadoSalud
# from ..enums.estadoSaludEnum import EstadoSalud

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(
        max_length=20,
        choices=RazaPerro.choices,
        default=RazaPerro.OTRO
    )
    edad = models.PositiveIntegerField(default=0) 
    tamaño = models.CharField(max_length=50, default=0)
    peso = models.FloatField(default=0)
    estado_salud =  models.CharField(
        max_length=20,
        choices=EstadoSalud.choices,
        default=EstadoSalud.SALUDABLE
    )
    vacunado = models.BooleanField(default=False)
    estado_adopcion = models.CharField(max_length=50, default='disponible')

    def __str__(self):
        return f"{self.nombre} ({self.raza})"

    def Adoptar(self):
        if self.estado_adopcion == "disponible":
            self.estado_adopcion = "adoptado"
            print(f"{self.nombre} ha sido adoptado.")
        else:
            print(f"{self.nombre} no está disponible para adopción.")
        
    def MostrarInfo(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso} kg")
        print(f"Estado de salud: {self.estado_salud}")
        print(f"Vacunado: {'Sí' if self.vacunado else 'No'}")
        print(f"Estado de adopción: {self.estado_adopcion}")

    def ActualizarEstadoSalud(self, nuevo_estado):
        self.estado_salud = nuevo_estado
        print(f"El estado de salud de {self.nombre} ha sido actualizado a: {self.estado_salud}")

    def Vacunar(self):
        if not self.vacunado:
            self.vacunado = True
            print(f"{self.nombre} ha sido vacunado.")
        else:
            print(f"{self.nombre} ya está vacunado.")