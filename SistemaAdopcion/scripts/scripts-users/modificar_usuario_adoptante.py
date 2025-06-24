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

usuarios = UserService.listar_usuarios()
for usuario in usuarios:
    print(f"{usuario.id}: {usuario.user.username} ({usuario.user.first_name} {usuario.user.last_name})")

usuario_id = int(input("Ingrese el ID del usuario a modificar: "))
usuario = usuarios.get(id=usuario_id)

def mostrar_usuario(usuario):
    print(f"\nID: {usuario.id}")
    print(f"1. Nombre: {usuario.user.first_name}")
    print(f"2. Apellido: {usuario.user.last_name}")
    print(f"3. Email: {usuario.user.email}")
    print(f"4. Teléfono: {usuario.telefono}")
    print(f"5. Dirección: {usuario.direccion}")
    print(f"6. Raza preferida: {usuario.pref_raza}")
    print(f"7. Edad preferida: {usuario.pref_edad}")
    print(f"8. Tamaño preferido: {usuario.pref_tamaño}")
    print(f"9. Estado de salud preferido: {usuario.pref_estado_salud}")
    print("-" * 40)

while True:
    mostrar_usuario(usuario)
    print("\n¿Qué desea modificar?")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Email")
    print("4. Teléfono")
    print("5. Dirección")
    print("6. Raza preferida")
    print("7. Edad preferida")
    print("8. Tamaño preferido")
    print("9. Estado de salud preferido")
    print("10. Guardar y salir")
    print("-" * 40)

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        nuevo = input("Nuevo nombre: ")
        if nuevo: usuario.user.first_name = nuevo
        
    elif opcion == "2":
        nuevo = input("Nuevo apellido: ")
        if nuevo: usuario.user.last_name = nuevo

    elif opcion == "3":
        nuevo = input("Nuevo email: ")
        if nuevo: usuario.user.email = nuevo

    elif opcion == "4":
        nuevo = input("Nuevo teléfono: ")
        if nuevo: usuario.telefono = nuevo

    elif opcion == "5":
        nuevo = input("Nueva dirección: ")
        if nuevo: usuario.direccion = nuevo

    elif opcion == "6":
        print("Opciones de raza preferida:")
        print("-" * 40)
        for raza in RazaPerro:
            print(f"{raza.value}: {raza.label}")
        print("-" * 40)
        nuevo = input("Nuevo valor de raza preferida: ")
        if nuevo: usuario.pref_raza = nuevo

    elif opcion == "7":
        print("Opciones de edad preferida:")
        print("-" * 40)
        for edad in Edad:
            print(f"{edad.value}: {edad.label}")
        print("-" * 40)
        nuevo = input("Nuevo valor de edad preferida: ")
        if nuevo: usuario.pref_edad = nuevo

    elif opcion == "8":
        print("Opciones de tamaño preferido:")
        print("-" * 40)
        for tam in Tamaño:
            print(f"{tam.value}: {tam.label}")
        print("-" * 40)
        nuevo = input("Nuevo valor de tamaño preferido: ")
        if nuevo: usuario.pref_tamaño = nuevo

    elif opcion == "9":
        print("Opciones de estado de salud preferido:")
        print("-" * 40)
        for estado in EstadoSalud:
            print(f"{estado.value}: {estado.label}")
        print("-" * 40)
        nuevo = input("Nuevo valor de estado de salud preferido: ")
        if nuevo: usuario.pref_estado_salud = nuevo

    elif opcion == "10":
        usuario.user.save()
        usuario.save()
        print("-" * 40)
        print("¡Usuario modificado correctamente!")
        print("-" * 40)
        break
    else:
        print("-" * 40)
        print("Opción no válida. Intente de nuevo.")
        print("-" * 40)
