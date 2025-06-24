import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from perros import init_django
init_django('SistemaAdopcion.settings')

from perros.services.perro_service import PerroService
from perros.models import Perro
from perros.enums.estadoSaludEnum import EstadoSalud

print("Perros disponibles:")
for perro in Perro.objects.all():
    print(f"{perro.id}: {perro.nombre} ({perro.get_estado_salud_display()})")

perro_id = int(input("Ingrese el ID del perro a actualizar: "))
perro = Perro.objects.get(id=perro_id)

print("Opciones de estado de salud:")
for estado in EstadoSalud:
    print(f"{estado.value}: {estado.label}")

nuevo_estado = input("Ingrese el valor del nuevo estado de salud: ")

PerroService.actualizar_estado_salud(perro, nuevo_estado)
print("Estado de salud actualizado correctamente.")