import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from perros import init_django
init_django('SistemaAdopcion.settings')


from perros.services.sistema_adopcion_service import SistemaAdopcion
from perros.services.usuario_service import UserService

usuarios = UserService.listar_usuarios()
for usuario in usuarios:
    print(f"{usuario.id}: {usuario.user.username} ({usuario.user.first_name} {usuario.user.last_name})")

usuario_id = int(input("Ingrese el ID del usuario para ver su historial: "))
print("-" * 40)

SistemaAdopcion.ver_historial_adopciones(usuario_id)
