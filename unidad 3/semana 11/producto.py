class Producto:
    """
    Representa un producto en el inventario.
    """

    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # --------------------
    # Properties con validación
    # --------------------
    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El ID debe ser una cadena no vacía.")
        self._id_producto = valor.strip()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self._nombre = valor.strip()

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La cantidad debe ser un entero >= 0.")
        self._cantidad = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        try:
            v = float(valor)
        except:
            raise ValueError("El precio debe ser un número.")
        if v < 0:
            raise ValueError("El precio debe ser >= 0.")
        self._precio = v

    # --------------------
    # Representación
    # --------------------
    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: {self.precio}"

