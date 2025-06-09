# tradicional

def ingresar_temperaturas():
    """Devuelve una lista fija de temperaturas para la semana."""
    return [22.5, 23.0, 21.8, 24.1, 22.9, 23.3, 24.0]  # Temperaturas simuladas

def calcular_promedio(temperaturas):
    """Calcula el promedio de las temperaturas dadas."""
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)

def main():
    print("Promedio Semanal del Clima - Programación Tradicional")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"=== El promedio semanal de temperatura es: {promedio:.2f}°C ===")

if __name__ == "__main__":
    main()

# poo

class DiaClima:
    """Representa la temperatura de un solo día."""
    def __init__(self, temperatura):
        self.__temperatura = temperatura  # Encapsulamiento

    def obtener_temperatura(self):
        return self.__temperatura

class SemanaClima:
    """Representa una semana de datos climáticos."""
    def __init__(self):
        self.dias = []

    def agregar_dia(self, temperatura):
        dia = DiaClima(temperatura)
        self.dias.append(dia)

    def calcular_promedio(self):
        if not self.dias:
            return 0
        total = sum(dia.obtener_temperatura() for dia in self.dias)
        return total / len(self.dias)

def main():
    print("Promedio Semanal del Clima - POO")
    semana = SemanaClima()
    temperaturas = [20, 21.5, 22, 19, 23, 24, 22.8]
    for temp in temperaturas:
        semana.agregar_dia(temp)

    promedio = semana.calcular_promedio()
    print(f"===El promedio semanal de temperatura es: {promedio:.2f}°C ===")

if __name__ == "__main__":
    main()

"""
Comparación entre Programación Tradicional y Programación Orientada a Objetos (POO)

En este proyecto implementamos dos formas de calcular el promedio semanal del clima:

1. Programación Tradicional:
   - Usamos funciones simples para pedir datos y calcular el promedio.
   - Es un método sencillo, fácil de entender y rápido de escribir.
   - Funciona bien para programas pequeños o tareas específicas.
   - Pero, si el programa crece, puede volverse difícil de manejar y organizar.

2. Programación Orientada a Objetos (POO):
   - Organizamos el programa en clases que representan conceptos reales: un día y una semana de clima.
   - Cada clase tiene sus propias responsabilidades y métodos.
   - Esto hace el código más ordenado, modular y fácil de ampliar.
   - Es especialmente útil cuando el programa se vuelve más complejo o se quiere reutilizar código.

En resumen, ambos métodos funcionan para el problema que tenemos, pero la POO nos ayuda a crear programas más estructurados y preparados para crecer sin perder claridad.
"""
