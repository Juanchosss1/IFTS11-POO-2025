class UsuarioAdoptante:
    def __init__(self, nombre, apellido, email, telefono, direccion, preferencia_mascota=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.preferencia_mascota = preferencia_mascota
        self.perro_adoptado = None
        self.historial_adopciones = []  # Para guardar el historial

    def registrarse(self):
        print(f"Usuario registrado: {self.nombre} {self.apellido}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")

    def modificar_datos(self, nombre=None, apellido=None, email=None, telefono=None, direccion=None, preferencia_mascota=None):
        if nombre: self.nombre = nombre
        if apellido: self.apellido = apellido
        if email: self.email = email
        if telefono: self.telefono = telefono
        if direccion: self.direccion = direccion
        if preferencia_mascota: self.preferencia_mascota = preferencia_mascota
        print("Datos modificados correctamente.")

    def adoptar_perro(self, perro):
        self.perro_adoptado = perro
        self.historial_adopciones.append(perro)
        print(f"El usuario {self.nombre} ha adoptado a perro {perro.nombre}")

    def ver_historial(self):
        if not self.historial_adopciones:
            print("No hay historial de adopciones.")
        else:
            print("Historial de adopciones:")
            for perro in self.historial_adopciones:
                print(f"- {perro.nombre}")
