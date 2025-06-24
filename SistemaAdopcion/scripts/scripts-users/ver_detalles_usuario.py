import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from perros import init_django
init_django('SistemaAdopcion.settings')

from perros.services.usuario_service import UserService
from perros.models import UsuarioAdoptante

print("Usuarios:")
for usuario in UsuarioAdoptante.objects.all():
    print(f"{usuario.id}: {usuario.user.first_name} {usuario.user.last_name} ({usuario.user.email})")

usuario_id = int(input("Ingrese el ID del usuario para ver su detalle: "))
usuario = UsuarioAdoptante.objects.get(id=usuario_id)

print("-" * 40)
UserService.mostrar_detalle(usuario)
print("-" * 40)