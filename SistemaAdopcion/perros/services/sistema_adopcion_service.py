from perros.models import Perro, UsuarioAdoptante, Postulacion

class SistemaAdopcion:
    def asignar_perro_a_usuario(self, perro_id, usuario_id):
        perro = Perro.objects.get(id=perro_id)
        usuario = UsuarioAdoptante.objects.get(id=usuario_id)
        Postulacion.objects.create(usuario=usuario, perro=perro, confirmada=True)
        perro.estado_adopcion = "adoptado"
        perro.save()
        return perro

    def sugerir_perros(usuario):
        perros = Perro.objects.filter(estado_adopcion='disponible')
        recomendaciones = []

        for perro in perros:
            coincidencias = 0
            if perro.raza == usuario.pref_raza:
                coincidencias += 1
            if perro.edad == usuario.pref_edad:
                coincidencias += 1
            if perro.tamaño == usuario.pref_tamaño:
                coincidencias += 1
            if perro.estado_salud == usuario.pref_estado_salud:
                coincidencias += 1
            recomendaciones.append((perro, coincidencias))

        recomendaciones.sort(key=lambda x: x[1], reverse=True)

        if recomendaciones:
            max_coincidencias = recomendaciones[0][1]
            sugeridos = [perro for perro, c in recomendaciones if c == max_coincidencias and c > 0]
            return sugeridos
        else:
            return []