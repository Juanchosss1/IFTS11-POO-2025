class Perro:
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado_adopcion):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado_adopcion = estado_adopcion

        def Adoptar(self):
            if self.estado_adopcion == "disponible":
                self.estado_adopcion = "adoptado"
                print(f"{self.nombre} ha sido adoptado.")
            else:
                print(f"{self.nombre} no está disponible para adopción.")
        
        def MostrarInfo(self):
            print(f"Nombre: {self.nombre}")
            print(f"Raza: {self.raza}")
            print(f"Edad: {self.edad} años")
            print(f"Tamaño: {self.tamaño}")
            print(f"Peso: {self.peso} kg")
            print(f"Estado de salud: {self.estado_salud}")
            print(f"Vacunado: {'Sí' if self.vacunado else 'No'}")
            print(f"Estado de adopción: {self.estado_adopcion}")

        def ActualizarEstadoSalud(self, nuevo_estado):
            self.estado_salud = nuevo_estado
            print(f"El estado de salud de {self.nombre} ha sido actualizado a: {self.estado_salud}")

        def Vacunar(self):
            if not self.vacunado:
                self.vacunado = True
                print(f"{self.nombre} ha sido vacunado.")
            else:
                print(f"{self.nombre} ya está vacunado.")