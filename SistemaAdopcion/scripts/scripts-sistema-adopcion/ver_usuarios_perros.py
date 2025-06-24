import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from perros import init_django
init_django('SistemaAdopcion.settings')

from perros.services.sistema_adopcion_service import SistemaAdopcion

usuarios_con_perros = SistemaAdopcion.listar_usuarios_con_perros()
for usuario, perros in usuarios_con_perros:
    print(f"Usuario: {usuario.user.first_name} {usuario.user.last_name}")
    if perros:
        print(f"Perros:")
        for nombre_perro in perros:
            print(f"\t{nombre_perro}")
    else:
        print("\t(No ha adoptado perros)")
print("-" * 40)