class SistemaAdopcionService:
    def __init__(self):
        self.adoptantes = []
        self.adoptados = []

    def agregar_adoptante(self, adoptante):
        self.adoptantes.append(adoptante)

    def agregar_adoptado(self, adoptado):
        self.adoptados.append(adoptado)

    def eliminar_perro(self, perro):
        if perro in self.adoptados:
            self.adoptados.remove(perro)
            print(f"Perro {perro.nombre} eliminado de la lista de adoptados.")
        else:
            print(f"Perro {perro.nombre} no encontrado en la lista de adoptados.")
    
    def buscarPerroSegunPreferencia(self, preferencia):
        #agregar mas preferencias -> polimorfismo
        for perro in self.adoptados:
            if perro.raza == preferencia or perro.tamaño == preferencia:
                return perro
        return None
    
    def confirmarAdopcion(self, perro, adoptante):
        if perro in self.adoptados and adoptante in self.adoptantes:
            perro.Adoptar()
            adoptante.adoptar_perro(perro)
            print(f"Adopción confirmada: {adoptante.nombre} ha adoptado al perro {perro.nombre}.")
        else:
            print("No se puede confirmar la adopción. Verifique los datos.")

    def listar_adoptantes(self):
        return self.adoptantes

    def listar_adoptados(self):
        return self.adoptados
    