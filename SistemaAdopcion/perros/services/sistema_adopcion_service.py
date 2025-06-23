from perros.models import Perro, UsuarioAdoptante, Postulacion

class SistemaAdopcion:
    def listar_perros(self):
       return Perro.objects.all()
    
    def listar_perros_disponibles(self):
        return Perro.objects.filter(estado_adopcion='disponible')

    def agregar_perro(self, **kwargs):
        return Perro.objects.create(**kwargs)

    def eliminar_perro(self, perro_id):
        Perro.objects.filter(id=perro_id).delete()

    def asignar_perro_a_usuario(self, perro_id, usuario_id):
        perro = Perro.objects.get(id=perro_id)
        usuario = UsuarioAdoptante.objects.get(id=usuario_id)
        Postulacion.objects.create(usuario=usuario, perro=perro, confirmada=True)
        perro.estado_adopcion = "adoptado"
        perro.save()
        return perro

    def sugerir_perros(self, usuario):
        return Perro.objects.filter(
            estado_adopcion='disponible',
            raza=usuario.preferencia_mascota
        )