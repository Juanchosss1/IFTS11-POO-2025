import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from perros import init_django
init_django('SistemaAdopcion.settings')

from perros.models import Perro
from perros.enums.razaEnum import RazaPerro
from perros.enums.edadEnum import Edad
from perros.enums.tamañoEnum import Tamaño
from perros.enums.estadoSaludEnum import EstadoSalud
from perros.services.perro_service import PerroService

print("Perros disponibles:")
for perro in Perro.objects.all():
    print(f"{perro.id}: {perro.nombre} ({perro.get_raza_display()})")

perro_id = int(input("Ingrese el ID del perro a modificar: "))
perro = Perro.objects.get(id=perro_id)

while True:
    PerroService.mostrar_detalle(perro)

    print("-" * 40)
    print("\n¿Qué desea modificar?")
    print("-" * 40)
    print("1. Nombre")
    print("2. Raza")
    print("3. Edad")
    print("4. Tamaño")
    print("5. Peso")
    print("6. Estado de salud")
    print("7. Vacunado")
    print("8. Estado de adopción")
    print("9. Guardar y salir")
    print("-" * 40)
    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        nuevo = input("Nuevo nombre: ")
        if nuevo: perro.nombre = nuevo
    elif opcion == "2":
        print("Opciones de raza:")
        for raza in RazaPerro:
            print(f"{raza.value}: {raza.label}")
        nuevo = input("Nuevo valor de raza: ")
        if nuevo: perro.raza = nuevo
    elif opcion == "3":
        print("Opciones de edad:")
        for edad in Edad:
            print(f"{edad.value}: {edad.label}")
        nuevo = input("Nuevo valor de edad: ")
        if nuevo: perro.edad = nuevo
    elif opcion == "4":
        print("Opciones de tamaño:")
        for tam in Tamaño:
            print(f"{tam.value}: {tam.label}")
        nuevo = input("Nuevo valor de tamaño: ")
        if nuevo: perro.tamaño = nuevo
    elif opcion == "5":
        nuevo = input("Nuevo peso (kg): ")
        if nuevo: perro.peso = float(nuevo)
    elif opcion == "6":
        print("Opciones de estado de salud:")
        for estado in EstadoSalud:
            print(f"{estado.value}: {estado.label}")
        nuevo = input("Nuevo valor de estado de salud: ")
        if nuevo: perro.estado_salud = nuevo
    elif opcion == "7":
        nuevo = input("¿Vacunado? (s/n): ").lower()
        if nuevo == "s":
            perro.vacunado = True
        elif nuevo == "n":
            perro.vacunado = False
    elif opcion == "8":
        print("Opciones de estado de adopción:")
        print("1: Disponible")
        print("2: Adoptado")
        nuevo = input("Nuevo estado de adopción (valor): ")
        if nuevo in ["1", "2"]:
            perro.estado_adopcion = nuevo
    elif opcion == "9":
        perro.save()
        print("-" * 40)
        print("¡Perro modificado correctamente!")
        print("-" * 40)
        break
    else:
        print("-" * 40)
        print("Opción no válida. Ingrese otro numero (1-9).")
        print("-" * 40)