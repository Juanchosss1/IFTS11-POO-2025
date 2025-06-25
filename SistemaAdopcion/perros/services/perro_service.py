from perros.models import Perro

class PerroService:
    
    @staticmethod
    def ver_perros():
       return Perro.objects.all()
    
    @staticmethod
    def ver_perros_disponibles():
        return Perro.objects.filter(estado_adopcion='disponible')
    
    @staticmethod
    def agregar_perro(**perroDto):
        return Perro.objects.create(**perroDto)
    
    @staticmethod
    def eliminar_perro(perro_id):
        Perro.objects.filter(id=perro_id).delete()

    @staticmethod
    def adoptar(perro):
        if perro.estado_adopcion == 'disponible':
            perro.estado_adopcion = 'adoptado'
            perro.save()
            print(f"{perro.nombre} ha sido adoptado.")
        else:
            print(f"{perro.nombre} no está disponible para adopción.")

    @staticmethod
    def mostrar_detalle(perro):
        print(f"Nombre: {perro.nombre}")
        print(f"Raza: {perro.get_raza_display()}")
        print(f"Edad: {perro.edad} años")
        print(f"Tamaño: {perro.get_tamaño_display()}")
        print(f"Peso: {perro.peso} kg")
        print(f"Estado de salud: {perro.get_estado_salud_display()}")
        print(f"Vacunado: {'Sí' if perro.vacunado else 'No'}")
        print(f"Estado de adopción: {perro.get_estado_adopcion_display()}")

    @staticmethod
    def actualizar_estado_salud(perro, nuevo_estado):
        perro.estado_salud = nuevo_estado
        perro.save()
        print(f"El estado de salud de {perro.nombre} ha sido actualizado a: '{perro.get_estado_salud_display()}'")

    @staticmethod
    def vacunar(perro):
        if not perro.vacunado:
            perro.vacunado = True
            perro.save()
            print(f"{perro.nombre} ha sido vacunado.")
        else:
            print(f"{perro.nombre} ya está vacunado.")