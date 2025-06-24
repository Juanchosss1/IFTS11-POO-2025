import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from perros import init_django
init_django('SistemaAdopcion.settings')

from perros.services.usuario_service import UserService
from perros.enums.razaEnum import RazaPerro
from perros.enums.edadEnum import Edad
from perros.enums.tamañoEnum import Tamaño
from perros.enums.estadoSaludEnum import EstadoSalud

print("=== Crear nuevo usuario adoptante ===")
username = input("Nombre de usuario: ")
password = input("Contraseña: ")
email = input("Email: ")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
telefono = input("Teléfono: ")
direccion = input("Dirección: ")

print("-" * 40)
print("Opciones de raza preferida:")
print("-" * 40)
for raza in RazaPerro:
    print(f"{raza.value}: {raza.label}")
print("-" * 40)
pref_raza = input("Raza preferida (valor): ")
print("-" * 40)

print("Opciones de edad preferida:")
print("-" * 40)
for edad in Edad:
    print(f"{edad.value}: {edad.label}")
print("-" * 40)
pref_edad = input("Edad preferida (valor): ")

print("-" * 40)
print("Opciones de tamaño preferido:")
print("-" * 40)
for tam in Tamaño:
    print(f"{tam.value}: {tam.label}")
print("-" * 40)
pref_tamaño = input("Tamaño preferido (valor): ")

print("-" * 40)
print("Opciones de estado de salud preferido:")
print("-" * 40)
for estado in EstadoSalud:
    print(f"{estado.value}: {estado.label}")
print("-" * 40)
pref_estado_salud = input("Estado de salud preferido (valor): ")
print("-" * 40)

usuario = UserService.crear_usuario(
    username, password, email, nombre, apellido, telefono, direccion,
    pref_raza, pref_edad, pref_tamaño, pref_estado_salud
)
print(f"Usuario adoptante creado: {usuario.user.username} (ID: {usuario.id})")