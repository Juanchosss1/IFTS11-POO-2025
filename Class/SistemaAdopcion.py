class SistemaAdopcion:
    def __init__(self):
        self.perros = []         
        self.usuarios = []       
        self.postulaciones = {}  

    def cargar_perro(self, perro):
        self.perros.append(perro)
        print(f"Perro {perro.nombre} cargado al sistema.")

    def eliminar_perro(self, perro):
        if perro in self.perros:
            self.perros.remove(perro)
            print(f"Perro {perro.nombre} eliminado del sistema.")
        else:
            print("Perro no encontrado.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} registrado en el sistema.")

    def postular_perro(self, usuario, perro):
        if perro not in self.perros:
            print("Perro no disponible para adopción.")
            return
        if perro not in self.postulaciones:
            self.postulaciones[perro] = []
        self.postulaciones[perro].append(usuario)
        print(f"{usuario.nombre} se postuló para adoptar a {perro.nombre}.")

    def confirmar_adopcion(self, usuario, perro):
        if perro in self.perros and usuario in self.usuarios:
            usuario.adoptar_perro(perro)
            self.eliminar_perro(perro)
            print(f"Adopción confirmada: {usuario.nombre} adoptó a {perro.nombre}.")
        else:
            print("No se puede confirmar la adopción.")

    def sugerir_perros(self, usuario):
        sugeridos = [perro for perro in self.perros if usuario.preferencia_mascota in (None, perro.raza)]
        print("Perros sugeridos según preferencia:")
        for perro in sugeridos:
            print(f"- {perro.nombre} ({perro.raza})")
        return sugeridos

    def mostrar_perros_disponibles(self):
        print("Perros disponibles para adopción:")
        for perro in self.perros:
            print(f"- {perro.nombre} ({perro.raza})")

    def mostrar_perros_por_estado(self, estado):
        print(f"Perros con estado '{estado}':")
        for perro in self.perros:
            if hasattr(perro, 'estado') and perro.estado == estado:
                print(f"- {perro.nombre} ({perro.raza})")

    def mostrar_perros_por_usuario(self, usuario):
        print(f"Perros adoptados por {usuario.nombre}:")
        usuario.ver_historial()