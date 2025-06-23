import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from perros import init_django
init_django('SistemaAdopcion.settings')
from perros.services.sistema_adopcion_service import SistemaAdopcion

sistema = SistemaAdopcion()
for perro in sistema.listar_perros():
    print(f"{perro.id} - {perro.nombre} ({perro.get_raza_display()})")
print("-" * 40)
perro_id = int(input("Ingrese el ID del perro a eliminar: "))
sistema.eliminar_perro(perro_id)

print("Perro eliminado correctamente.")
print("-" * 40)
