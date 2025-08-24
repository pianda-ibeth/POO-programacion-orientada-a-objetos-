import json
import csv
from producto import Producto

class Inventario:
    """
    Clase que gestiona la colección de productos de una tienda.
    Utiliza un diccionario para búsqueda rápida por ID.
    """

    def __init__(self):
        self.productos = {}  # Diccionario {id_producto: Producto}

    # --------------------
    # CRUD
    # --------------------
    def añadir_producto(self, producto: Producto):
        """Agrega un nuevo producto al inventario."""
        if producto.id_producto in self.productos:
            print(" El ID ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            print(" Producto añadido correctamente.")

    def eliminar_producto(self, id_producto: str):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado correctamente.")
        else:
            print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto: str, cantidad: int = None, precio: float = None):
        """Actualiza la cantidad o precio de un producto."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print(" Producto actualizado correctamente.")
        else:
            print(" Producto no encontrado.")

    # --------------------
    # Búsqueda y visualización
    # --------------------
    def buscar_producto(self, nombre: str):
        """Busca y devuelve productos que contengan el nombre dado."""
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return encontrados if encontrados else None

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print(" Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def valor_total_inventario(self):
        """Calcula el valor total del inventario (cantidad × precio)."""
        total = sum(p.cantidad * p.precio for p in self.productos.values())
        return total

    # --------------------
    # Persistencia JSON
    # --------------------
    def guardar_en_archivo(self, archivo="inventario.json"):
        """Guarda el inventario en un archivo JSON."""
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump({id_: vars(p) for id_, p in self.productos.items()}, f, indent=4)
        print(" Inventario guardado en archivo JSON.")

    def cargar_desde_archivo(self, archivo="inventario.json"):
        """Carga el inventario desde un archivo JSON."""
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = {id_: Producto(**p) for id_, p in data.items()}
            print(" Inventario cargado desde archivo JSON.")
        except FileNotFoundError:
            print(" Archivo JSON no encontrado, se iniciará un inventario vacío.")

    # --------------------
    # Exportar a CSV
    # --------------------
    def exportar_csv(self, archivo="inventario.csv"):
        """Exporta todos los productos a un archivo CSV."""
        if not self.productos:
            print("️ No hay productos para exportar.")
            return
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nombre", "Cantidad", "Precio"])
            for p in self.productos.values():
                writer.writerow([p.id_producto, p.nombre, p.cantidad, p.precio])
        print(f" Inventario exportado a {archivo}")
