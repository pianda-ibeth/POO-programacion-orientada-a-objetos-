# mascotas.py

# Clase base que representa una mascota
class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre       # Atributo público
        self.__edad = edad         # Atributo privado (encapsulado)

    # Método para obtener la edad (encapsulamiento)
    def obtener_edad(self):
        return self.__edad

    # Método para establecer la edad (encapsulamiento)
    def establecer_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida")

    # Método que será sobrescrito por las clases derivadas (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")

# Clase derivada que hereda de Mascota
class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.raza = raza

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Otra clase derivada
class Gato(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

# --- PROGRAMA PRINCIPAL ---

# Crear instancias de las clases
mi_perro = Perro("Firulais", 5, "Labrador")
mi_gato = Gato("Michi", 3, "Blanco")

# Uso de métodos públicos
print(f"{mi_perro.nombre} tiene {mi_perro.obtener_edad()} años.")
print(f"{mi_gato.nombre} tiene {mi_gato.obtener_edad()} años.")

# Polimorfismo: mismo método en distintas clases con diferente comportamiento
mi_perro.hacer_sonido()
mi_gato.hacer_sonido()

# Encapsulamiento en acción
mi_perro.establecer_edad(6)
print(f"Ahora {mi_perro.nombre} tiene {mi_perro.obtener_edad()} años.")
