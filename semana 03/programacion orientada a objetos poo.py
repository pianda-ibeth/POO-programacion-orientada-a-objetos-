# poo.py

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




