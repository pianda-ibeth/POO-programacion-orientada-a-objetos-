class Libro:
    """
    Clase que representa un libro en la biblioteca digital.
    Utiliza tuplas para los atributos inmutables como autor y título.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Uso de tuplas para atributos inmutables
        self.titulo_autor = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        disponibilidad = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo_autor[0]}' por {self.titulo_autor[1]} - {self.categoria} (ISBN: {self.isbn}) - {disponibilidad}"

    def obtener_titulo(self):
        return self.titulo_autor[0]

    def obtener_autor(self):
        return self.titulo_autor[1]