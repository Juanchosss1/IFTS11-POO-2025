import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from perros import init_django
init_django('SistemaAdopcion.settings')


from perros.services.perro_service import PerroService

print("Perros:")
print('-'*40)
for perro in PerroService.ver_perros_disponibles():
    print(f"{perro.nombre} ({perro.get_raza_display()})")