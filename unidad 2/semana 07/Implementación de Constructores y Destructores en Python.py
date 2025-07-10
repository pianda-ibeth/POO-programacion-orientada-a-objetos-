# archivo: estudiante.py

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        """
        Constructor de la clase Estudiante.
        Se ejecuta al crear un nuevo estudiante, inicializando sus datos personales.
        """
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"[INIT] Estudiante creado: {self.nombre}, {self.edad} años, carrera: {self.carrera}")

    def mostrar_info(self):
        """
        Muestra la información del estudiante.
        """
        print(f"[INFO] Nombre: {self.nombre}")
        print(f"[INFO] Edad: {self.edad}")
        print(f"[INFO] Carrera: {self.carrera}")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta cuando el objeto es destruido.
        Aquí simula la eliminación de datos del estudiante del sistema.
        """
        print(f"[DEL] Eliminando datos del estudiante: {self.nombre}")

# Uso del programa
if __name__ == "__main__":
    print("[MAIN] Inicio del programa de gestión de estudiantes")

    estudiante1 = Estudiante("Ana Torres", 20, "Ingeniería Informática")
    estudiante2 = Estudiante("Carlos Pérez", 22, "Administración de Empresas")

    print("\n[MAIN] Mostrando información de estudiantes:\n")
    estudiante1.mostrar_info()
    print()
    estudiante2.mostrar_info()

    print("\n[MAIN] Fin del programa (los destructores se llamarán automáticamente)")
