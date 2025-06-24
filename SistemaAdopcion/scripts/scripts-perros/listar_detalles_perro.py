import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from perros import init_django
init_django('SistemaAdopcion.settings')

from perros.services.perro_service import PerroService
from perros.models import Perro

print("Perros disponibles:")
for perro in Perro.objects.all():
    print(f"{perro.id}: {perro.nombre} ({perro.get_estado_salud_display()})")

perro_id = int(input("Ingrese el ID del perro para ver su detalle: "))

for perro in Perro.objects.filter(id=perro_id):
    print("-" * 40)
    print(f"{perro.nombre.upper()}")
    print("-" * 40)
    perro.MostrarInfo()