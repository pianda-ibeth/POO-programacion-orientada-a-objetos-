import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        """Añade un producto verificando que el ID sea único"""
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID"""
        for p in self.productos:
            if p.id_producto == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print(" Producto eliminado.")
                return
        print("No se encontró el producto.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza cantidad o precio de un producto"""
        for p in self.productos:
            if p.id_producto == id_producto:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                self.guardar_en_archivo()
                print("Producto actualizado.")
                return
        print("No se encontró el producto.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre (puede haber varios con nombre similar)"""
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        """Muestra todos los productos"""
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for p in self.productos:
                print(p)

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo de texto"""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(f"{p.id_producto},{p.nombre},{p.cantidad},{p.precio}\n")
        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo.")

    def cargar_desde_archivo(self):
        """Carga los productos desde un archivo, si no existe lo crea con datos de ejemplo"""
        if not os.path.exists(self.archivo):
            self.cargar_datos_ejemplo()
            self.guardar_en_archivo()
        else:
            try:
                with open(self.archivo, "r", encoding="utf-8") as f:
                    for linea in f:
                        datos = linea.strip().split(",")
                        if len(datos) == 4:
                            id_producto, nombre, cantidad, precio = datos
                            self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
            except FileNotFoundError:
                print("Archivo no encontrado, creando uno nuevo.")
                self.cargar_datos_ejemplo()
                self.guardar_en_archivo()
            except ValueError:
                print("Error en los datos del archivo. Se usarán datos de ejemplo.")
                self.cargar_datos_ejemplo()
                self.guardar_en_archivo()

    def cargar_datos_ejemplo(self):
        """Carga datos iniciales para pruebas"""
        self.productos = [
            Producto("P001", "Arroz", 50, 1.20),
            Producto("P002", "Azúcar", 30, 0.90),
            Producto("P003", "Aceite", 20, 3.50),
            Producto("P004", "Leche", 40, 0.80),
            Producto("P004", "Leche", 40, 0.80),
            Producto("P005", "Huevos", 50, 4),
            Producto("P006", "Pan", 100, 1.75),
            Producto("P007", "Sal", 60, 1.10),
            Producto("P008", "Cafe", 35, 2),
            Producto("P009", "fideos", 45, 1.50),
            Producto("P010", "Atun", 70, 1.55),

        ]
