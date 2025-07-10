class Vehiculo:
    def __init__(self, placa):
        self.placa = placa
        print(f"Vehículo {self.placa} ingresó al parqueadero.")

    def __del__(self):
        print(f"Vehículo {self.placa} salió del parqueadero.")


def entrada_y_salida():
    vehiculo = Vehiculo("ABC-123")
entrada_y_salida()