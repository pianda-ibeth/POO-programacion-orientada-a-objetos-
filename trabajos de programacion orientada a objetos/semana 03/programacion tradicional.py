# tradicional.py

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
