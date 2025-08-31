class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    Utiliza una lista para gestionar los libros prestados al usuario.
    """

    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"

    def tomar_prestado(self, libro):
        """Añade un libro a la lista de libros prestados"""
        self.libros_prestados.append(libro)
        libro.disponible = False

    def devolver(self, libro):
        """Remueve un libro de la lista de libros prestados"""
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            libro.disponible = True
            return True
        return False

    def listar_libros_prestados(self):
        """Devuelve una lista de los libros actualmente prestados"""
        return [str(libro) for libro in self.libros_prestados]