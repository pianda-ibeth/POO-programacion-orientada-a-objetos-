# tienda_online.py

# Clase Producto representa un artículo en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

# Clase Cliente representa a una persona que realiza compras
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.actualizar_stock(-cantidad)
            print(f"{cantidad}x {producto.nombre} agregado al carrito.")
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    def ver_carrito(self):
        print(f"\nCarrito de {self.nombre}:")
        total = 0
        for item, cantidad in self.carrito:
            subtotal = item.precio * cantidad
            print(f"- {cantidad}x {item.nombre} = ${subtotal}")
            total += subtotal
        print(f"Total: ${total}\n")

# Clase Tienda que administra productos y clientes
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"\nCatálogo de {self.nombre}:")
        for producto in self.productos:
            print(producto.mostrar_info())

# ----- Simulación -----

# Crear productos
p1 = Producto("Laptop", 1200, 5)
p2 = Producto("Mouse", 25, 20)
p3 = Producto("Teclado", 45, 15)

# Crear tienda y agregar productos
mi_tienda = Tienda("Tech Store")
mi_tienda.agregar_producto(p1)
mi_tienda.agregar_producto(p2)
mi_tienda.agregar_producto(p3)

# Mostrar productos disponibles
mi_tienda.mostrar_productos()

# Crear cliente y simular compras
cliente1 = Cliente("Ibeth")
cliente1.agregar_al_carrito(p1, 1)
cliente1.agregar_al_carrito(p2, 2)

# Ver el carrito del cliente
cliente1.ver_carrito()

# Mostrar productos después de la compra para ver el cambio en el stock
mi_tienda.mostrar_productos()
