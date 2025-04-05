

class BaseDeDatos:
    def __init__(self):
        self.tareas = []  

    def guardar_tarea(self, tarea):
        self.tareas.append(tarea)
        return f"Tarea guardada: {tarea}"  


class Backend:
    def __init__(self, db):
        self.db = db

    def procesar_tarea(self, tarea):
        if not tarea.strip(): 
            return "Error: La tarea no puede estar vacía."
        return self.db.guardar_tarea(tarea)  


def frontend():
    db = BaseDeDatos()
    backend = Backend(db)
    
    while True:
        tarea = input("Ingrese una tarea (o 'salir' para terminar): ")
        if tarea.lower() == 'salir':
            break
        respuesta = backend.procesar_tarea(tarea)
        print(respuesta) 

# Ejecutar la mini app
test_mode = __name__ == "__main__"
if test_mode:
    frontend()
