# Sistema de Adopción de Perros

Este proyecto permite gestionar perros, usuarios adoptantes y el proceso de adopción.

---

## Servicios y Métodos

### **PerroService**

- **listar_perros()**
  - Devuelve todos los perros registrados.
- **ver_perros_disponibles()**
  - Devuelve todos los perros con estado de adopción "disponible".
- **agregar_perro(**datos)**
  - Crea un nuevo perro con los datos recibidos.
- **mostrar_info(perro)**
  - Muestra por consola todos los detalles del perro.
- **actualizar_estado_salud(perro, nuevo_estado)**
  - Cambia el estado de salud del perro y lo guarda.
- **vacunar(perro)**
  - Marca al perro como vacunado y lo guarda.

### **UserService**

- **listar_usuarios()**
  - Devuelve todos los usuarios adoptantes.
- **crear_usuario(username, password, email, nombre, apellido, telefono, direccion, pref_raza, pref_edad, pref_tamaño, pref_estado_salud)**
  - Crea un usuario adoptante con preferencias.
- **mostrar_detalle(usuario)**
  - Muestra por consola todos los detalles del usuario adoptante.
- **modificar_usuario(usuario, **datos)**
  - Modifica los datos del usuario adoptante.
- **eliminar_usuario(usuario)**
  - Elimina el usuario adoptante y su usuario de Django.

### **SistemaAdopcion**

- **adoptar_perro(usuario_id, perro_id)**
  - Asigna un perro a un usuario, cambia el estado del perro a "adoptado" y registra la adopción en el historial (`Postulacion`).
- **sugerir_perros(usuario)**
  - Devuelve una lista numerada de perros disponibles, ordenados por coincidencias con las preferencias del usuario.  
    Ejemplo de resultado:
    ```
    1. Rocky (coincidencias: 3)
    2. Luna (coincidencias: 2)
    ```
- **ver_historial_adopciones(usuario_id)**
  - Muestra todos los perros adoptados por un usuario, incluyendo la fecha de adopción.  
    Ejemplo de salida:
    ```
    Historial de adopciones de Juan Pérez:
    - Rocky (adoptado el 24/06/2025 15:30)
    - Luna (adoptado el 25/06/2025 10:12)
    Total de perros adoptados: 2
    ```
- **ver_usuarios_con_perros()**
  - Devuelve una lista de tuplas `(usuario, [nombres_perros])` con todos los usuarios y los perros que han adoptado.

---

## Ejemplo de uso en scripts

### Crear un perro

```python
from perros.services.perro_service import PerroService

perro = PerroService.agregar_perro(
    nombre="Rocky",
    raza="labrador",
    edad="adulto",
    tamaño="grande",
    peso=25,
    estado_salud="saludable",
    vacunado=True,
    estado_adopcion="disponible"
)
```

### Crear un usuario adoptante

```python
from perros.services.usuario_service import UserService

usuario = UserService.crear_usuario(
    username="juan123",
    password="secreto",
    email="juan@mail.com",
    nombre="Juan",
    apellido="Pérez",
    telefono="12345678",
    direccion="Calle Falsa 123",
    pref_raza="labrador",
    pref_edad="adulto",
    pref_tamaño="grande",
    pref_estado_salud="saludable"
)
```

### Adoptar un perro

```python
from perros.services.sistema_adopcion_service import SistemaAdopcion

SistemaAdopcion.adoptar_perro(usuario_id=1, perro_id=2)
```

### Ver historial de adopciones

```python
SistemaAdopcion.ver_historial_adopciones(usuario_id=1)
```

### Sugerir perros para un usuario

```python
recomendaciones = SistemaAdopcion.sugerir_perros(usuario)
for linea in recomendaciones:
    print(linea)
```

### Listar usuarios con sus perros adoptados

```python
usuarios_con_perros = SistemaAdopcion.ver_usuarios_con_perros()
for usuario, perros in usuarios_con_perros:
    print(f"{usuario.user.first_name} {usuario.user.last_name}:")
    if perros:
        for nombre_perro in perros:
            print(f"  - {nombre_perro}")
    else:
        print("  (No ha adoptado perros)")
```

---

## Estructura recomendada de carpetas

```
SistemaAdopcion/
├── perros/
│   ├── models/
│   ├── services/
│   │   ├── perro_service.py
│   │   ├── usuario_service.py
│   │   └── sistema_adopcion_service.py
├── scripts/
│   ├── scripts-perros/
│   ├── scripts-users/
│   └── scripts-sistema-adopcion/
│       ├── adoptar_perro.py
│       ├── ver_usuarios_perros.py
│       └── ...
```

---

## Notas

- Todos los métodos de los servicios son estáticos y se llaman directamente desde la clase.
- Los scripts deben ejecutarse desde la raíz del proyecto para que los imports funcionen correctamente.
- El historial de adopciones se gestiona con el modelo `Postulacion` y el campo `confirmada=True`. La fecha de adopción se guarda automáticamente.

---

¿Dudas o sugerencias? ¡No dudes en consultar!