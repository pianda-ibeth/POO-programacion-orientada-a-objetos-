from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print(" Error: El ID ya existe.")
        else:
            self.productos.append(producto)
            print(" Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(" Producto eliminado.")
                return
        print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(" Producto actualizado.")
                return
        print(" Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print(" Resultados de búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print(" No se encontraron productos.")

    def mostrar_todos(self):
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print(" Lista de productos:")
            for p in self.productos:
                print(p)

    def cargar_datos_ejemplo(self):
        """Carga datos iniciales para pruebas"""
        self.añadir_producto(Producto("P001", "Arroz", 50, 1.20))
        self.añadir_producto(Producto("P002", "Azúcar", 30, 0.90))
        self.añadir_producto(Producto("P003", "Aceite", 20, 3.50))
        self.añadir_producto(Producto("P004", "Leche", 40, 0.80))
        self.añadir_producto(Producto("P005","Huevos",50,4))
        self.añadir_producto(Producto("P006","Pan",100,1.75))
        self.añadir_producto(Producto("P007","Sal",60,1.10))
        self.añadir_producto(Producto("P008","Cafe",35,2))
        self.añadir_producto(Producto("P009","fideos",45,1.50))
        self.añadir_producto(Producto("P010","Atun",70,1.55))

