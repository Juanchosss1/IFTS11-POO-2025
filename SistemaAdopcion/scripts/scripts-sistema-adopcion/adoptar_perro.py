import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
from perros import init_django
init_django('SistemaAdopcion.settings')


from perros.services.sistema_adopcion_service import SistemaAdopcion
from perros.services.usuario_service import UserService
from perros.services.perro_service import PerroService

usuarios = UserService.listar_usuarios()
for usuario in usuarios:
    print(f"{usuario.id}: {usuario.user.username} ({usuario.user.first_name} {usuario.user.last_name})")

usuario_id = int(input("Ingrese el ID del usuario que adoptara el perro: "))

if(len(PerroService.ver_perros_disponibles()) <= 0):
        print("-" * 40)
        print("No hay perros disponibles para adopción.")
        print("-" * 40)
        sys.exit(0)

print("-" * 40)
print("Perros disponibles para adopción:")
print("-" * 40)
for perro in PerroService.ver_perros_disponibles():    
    print(f"{perro.id} - {perro.nombre} ({perro.get_raza_display()})")
print("-" * 40)
perro_id = int(input("Ingrese el ID del perro a adoptar: "))

SistemaAdopcion.adoptar_perro(usuario_id, perro_id)
print("Perro adoptado correctamente.")