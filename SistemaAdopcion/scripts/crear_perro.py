import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from perros import init_django
init_django('SistemaAdopcion.settings')

from perros.services.sistema_adopcion_service import SistemaAdopcion
from perros.enums.razaEnum import RazaPerro
from perros.enums.estadoSaludEnum import EstadoSalud
from perros.enums.edadEnum import Edad
from perros.enums.tamañoEnum import Tamaño

sistema = SistemaAdopcion()

print("=== Crear nuevo perro ===")
nombre = input("Nombre: ")

print("-" * 40)
print("Opciones de raza:")
for raza in RazaPerro:
    print(f"{raza.value}: {raza.label}")
raza = input("Raza (elija un numero): ")

print("-" * 40)
print("Opciones de edad:")
for edad in Edad:
    print(f"{edad.value}: {edad.label}")
edad = input("Edad (elija un numero): ")

print("-" * 40)
print("Opciones de tamaño:")
for tam in Tamaño:
    print(f"{tam.value}: {tam.label}")
tamaño = input("Tamaño (elija un numero): ")

print("-" * 40)
peso = float(input("Peso (kg): "))

print("-" * 40)
print("Opciones de estado de salud:")
for estado in EstadoSalud:
    print(f"{estado.value}: {estado.label}")
estado_salud = input("Estado de salud (elija un numero): ")

print("-" * 40)
vacunado = input("¿Vacunado? (s/n): ").lower() == 's'

perro = sistema.agregar_perro(
    nombre=nombre,
    raza=raza,
    edad=edad,
    tamaño=tamaño,
    peso=peso,
    estado_salud=estado_salud,
    vacunado=vacunado,
    estado_adopcion='disponible'
)

print(f"Perro creado: {perro.nombre} (ID: {perro.id})")