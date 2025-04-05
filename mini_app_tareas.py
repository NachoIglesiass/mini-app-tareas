# mini_app_tareas.py

# ----- Base de Datos (Simulada) -----
class BaseDeDatos:
    def __init__(self):
        self.tareas = []  # Simulación de almacenamiento

    def guardar_tarea(self, tarea):
        self.tareas.append(tarea)
        return f"Tarea guardada: {tarea}"  # Respuesta del backend

# ----- Backend -----
class Backend:
    def __init__(self, db):
        self.db = db

    def procesar_tarea(self, tarea):
        if not tarea.strip():  # Validación de datos
            return "Error: La tarea no puede estar vacía."
        return self.db.guardar_tarea(tarea)  # Guardado en la base de datos

# ----- Frontend (Simulado en Consola) -----
def frontend():
    db = BaseDeDatos()
    backend = Backend(db)
    
    while True:
        tarea = input("Ingrese una tarea (o 'salir' para terminar): ")
        if tarea.lower() == 'salir':
            break
        respuesta = backend.procesar_tarea(tarea)
        print(respuesta)  # Simulación de la respuesta del backend

# Ejecutar la mini app
test_mode = __name__ == "__main__"
if test_mode:
    frontend()
