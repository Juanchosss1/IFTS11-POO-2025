from perros.models import Perro, UsuarioAdoptante, Postulacion

class SistemaAdopcion:
    @staticmethod
    def adoptar_perro(usuario_id, perro_id):
        usuario = UsuarioAdoptante.objects.get(id=usuario_id)
        perro = Perro.objects.get(id=perro_id)
        if perro.estado_adopcion == "adoptado":
            print(f"El perro {perro.nombre} ya fue adoptado.")
            return None

        Postulacion.objects.create(
            usuario=usuario,
            perro=perro,
            confirmada=True
        )

        perro.estado_adopcion = "adoptado"
        perro.save()
        print(f"¡{usuario.user.first_name} adoptó a {perro.nombre}!")
        return perro

    @staticmethod
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

        resultado = []
        for idx, (perro, coincidencias) in enumerate(recomendaciones, 1):
            resultado.append(f"{idx}. {perro.nombre} (coincidencias: {coincidencias})")

        return resultado
    
    @staticmethod
    def ver_historial_adopciones(usuario_id):
        usuario = UsuarioAdoptante.objects.get(id=usuario_id)
        historial = Postulacion.objects.filter(usuario=usuario, confirmada=True).order_by('fecha')
        print(f"Historial de adopciones de {usuario.user.first_name} {usuario.user.last_name}:")
        for postulacion in historial:
            fecha_str = postulacion.fecha.strftime("%d/%m/%Y %H:%M")
            print(f"- {postulacion.perro.nombre} (adoptado el {fecha_str})")
        print(f"Total de perros adoptados: {historial.count()}")
        return historial
    
    @staticmethod
    def ver_usuarios_con_perros():
        usuarios = UsuarioAdoptante.objects.all()
        resultado = []
        for usuario in usuarios:
            postulaciones = Postulacion.objects.filter(usuario=usuario, confirmada=True)
            perros = [postulacion.perro.nombre for postulacion in postulaciones]
            resultado.append((usuario, perros))
        return resultado