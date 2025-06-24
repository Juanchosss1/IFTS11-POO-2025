import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from perros import init_django
init_django('SistemaAdopcion.settings')


from perros.services.sistema_adopcion_service import SistemaAdopcion
from perros.services.usuario_service import UserService

print("Elija un usuario adoptante para sugerir perros:")
print("-" * 40)

usuarios = UserService.listar_usuarios()
for usuario in usuarios:
    print(f"{usuario.id}: {usuario.user.username} ({usuario.user.first_name} {usuario.user.last_name})")

print("-" * 40)
usuario_id = int(input("Ingrese el ID del usuario para sugerir un perro: "))

sugeridos = SistemaAdopcion.sugerir_perros(usuario)
print("En base a sus preferencias, los perros sugeridos son:")
print("-" * 40)
for perro in sugeridos:
    print(perro)
print("-" * 40)
