import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from perros import init_django

init_django('SistemaAdopcion.settings')

from perros.services.sistema_adopcion_service import SistemaAdopcion

sistema = SistemaAdopcion()
print("Perros en adopción:")
for perro in sistema.ver_perros_disponibles():
    print(f"{perro.nombre} ({perro.get_raza_display()})")