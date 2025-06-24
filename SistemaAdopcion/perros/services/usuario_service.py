from perros.models.usuario_adoptante import UsuarioAdoptante
from django.contrib.auth.models import User

class UserService:
    
    @staticmethod
    def listar_usuarios():
       return User.objects.all()
    
    @staticmethod
    def crear_usuario(username, password, email, nombre, apellido, telefono, direccion, pref_raza, pref_edad, pref_tamaño, pref_estado_salud):
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=nombre,
            last_name=apellido
        )
        return UsuarioAdoptante.objects.create(
            user=user,
            telefono=telefono,
            direccion=direccion,
            pref_raza=pref_raza,
            pref_edad=pref_edad,
            pref_tamaño=pref_tamaño,
            pref_estado_salud=pref_estado_salud
        )

    @staticmethod
    def modificar_usuario(usuario, **userDto):
        user = usuario.user
        if 'nombre' in userDto and userDto['nombre']:
            user.first_name = userDto['nombre']
        if 'apellido' in userDto and userDto['apellido']:
            user.last_name = userDto['apellido']
        if 'email' in userDto and userDto['email']:
            user.email = userDto['email']
        user.save()
        for campo in ['telefono', 'direccion', 'pref_raza', 'pref_edad', 'pref_tamaño', 'pref_estado_salud']:
            if campo in userDto and userDto[campo]:
                setattr(usuario, campo, userDto[campo])
        usuario.save()
        return usuario

    @staticmethod
    def eliminar_usuario(usuario):
        usuario.user.delete()  # Esto elimina también UsuarioAdoptante por OneToOne

    @staticmethod
    def listar_usuarios():
        return UsuarioAdoptante.objects.all()