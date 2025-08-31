from Libro import Libro
from Usuario import Usuario
import os
from datetime import datetime


class Biblioteca:
    """
    Clase principal que gestiona la biblioteca digital.
    Ahora guarda TODOS los datos en un solo archivo TXT.
    """

    def __init__(self):
        self.libros = {}  # Diccionario: ISBN -> Objeto Libro
        self.usuarios = {}  # Diccionario: ID usuario -> Objeto Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos
        self.historial_prestamos = []  # Lista para historial de préstamos
        self.data_file = "data/biblioteca_data.txt"
        self.crear_directorio_data()
        self.cargar_datos()

    def crear_directorio_data(self):
        """Crea el directorio data si no existe"""
        if not os.path.exists("data"):
            os.makedirs("data")

    def inicializar_datos_por_defecto(self):
        """Inicializa la biblioteca con 10 libros y 5 usuarios predefinidos"""
        print("📝 Inicializando con datos por defecto...")

        # 10 libros clásicos con ISBN reales
        libros_data = [
            ("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "9788437604947"),
            ("1984", "George Orwell", "Ciencia ficción", "9780451524935"),
            ("El principito", "Antoine de Saint-Exupéry", "Fábula", "9780156012195"),
            ("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela clásica", "9788424115266"),
            ("Crimen y castigo", "Fiódor Dostoyevski", "Novela psicológica", "9788491053178"),
            ("Orgullo y prejuicio", "Jane Austen", "Novela romántica", "9788491051280"),
            ("El señor de los anillos", "J.R.R. Tolkien", "Fantasía épica", "9788445000667"),
            ("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", "9788478884456"),
            ("La sombra del viento", "Carlos Ruiz Zafón", "Novela misterio", "9788408094355"),
            ("Rayuela", "Julio Cortázar", "Novela experimental", "9788432216420")
        ]

        for titulo, autor, categoria, isbn in libros_data:
            self.libros[isbn] = Libro(titulo, autor, categoria, isbn)

        # 5 usuarios predefinidos
        usuarios_data = [
            ("Ana García López", "U001"),
            ("Carlos Martínez Ruiz", "U002"),
            ("María Rodríguez Sánchez", "U003"),
            ("Pedro Fernández Gómez", "U004"),
            ("Laura Díaz Romero", "U005")
        ]

        for nombre, id_usuario in usuarios_data:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios[id_usuario] = usuario
            self.ids_usuarios.add(id_usuario)

        print("✅ 10 libros y 5 usuarios creados por defecto!")

    def guardar_datos(self):
        """Guarda TODOS los datos en un solo archivo TXT"""
        try:
            with open(self.data_file, "w", encoding="utf-8") as f:
                # Escribir encabezado de LIBROS
                f.write("[LIBROS]\n")
                for isbn, libro in self.libros.items():
                    f.write(
                        f"LIBRO|{isbn}|{libro.obtener_titulo()}|{libro.obtener_autor()}|{libro.categoria}|{libro.disponible}\n")

                # Escribir encabezado de USUARIOS
                f.write("\n[USUARIOS]\n")
                for id_usuario, usuario in self.usuarios.items():
                    libros_prestados = ",".join([libro.isbn for libro in usuario.libros_prestados])
                    f.write(f"USUARIO|{id_usuario}|{usuario.nombre}|{libros_prestados}\n")

                # Escribir encabezado de PRÉSTAMOS
                f.write("\n[PRESTAMOS]\n")
                for prestamo in self.historial_prestamos:
                    f.write(
                        f"PRESTAMO|{prestamo['fecha']}|{prestamo['accion']}|{prestamo['isbn']}|{prestamo['id_usuario']}\n")

            print("💾 Datos guardados exitosamente!")
        except Exception as e:
            print(f"❌ Error guardando datos: {e}")

    def cargar_datos(self):
        """Carga TODOS los datos desde un solo archivo TXT"""
        try:
            if not os.path.exists(self.data_file):
                print("📝 Archivo de datos no encontrado.")
                self.inicializar_datos_por_defecto()
                self.guardar_datos()  # Guardar los datos por defecto
                return

            print("📂 Cargando datos desde archivo...")
            with open(self.data_file, "r", encoding="utf-8") as f:
                seccion_actual = None

                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue

                    # Detectar secciones
                    if linea == "[LIBROS]":
                        seccion_actual = "LIBROS"
                        continue
                    elif linea == "[USUARIOS]":
                        seccion_actual = "USUARIOS"
                        continue
                    elif linea == "[PRESTAMOS]":
                        seccion_actual = "PRESTAMOS"
                        continue

                    # Procesar según la sección
                    if seccion_actual == "LIBROS" and linea.startswith("LIBRO|"):
                        datos = linea.split("|")
                        if len(datos) == 6:
                            _, isbn, titulo, autor, categoria, disponible = datos
                            libro = Libro(titulo, autor, categoria, isbn)
                            libro.disponible = disponible.lower() == "true"
                            self.libros[isbn] = libro

                    elif seccion_actual == "USUARIOS" and linea.startswith("USUARIO|"):
                        datos = linea.split("|")
                        if len(datos) >= 4:
                            _, id_usuario, nombre, libros_prestados_str = datos[0], datos[1], datos[2], datos[3]
                            usuario = Usuario(nombre, id_usuario)
                            self.usuarios[id_usuario] = usuario
                            self.ids_usuarios.add(id_usuario)

                            # Cargar libros prestados
                            if libros_prestados_str:
                                for isbn in libros_prestados_str.split(","):
                                    if isbn in self.libros:
                                        usuario.tomar_prestado(self.libros[isbn])

                    elif seccion_actual == "PRESTAMOS" and linea.startswith("PRESTAMO|"):
                        datos = linea.split("|")
                        if len(datos) == 5:
                            _, fecha, accion, isbn, id_usuario = datos
                            self.historial_prestamos.append({
                                'fecha': fecha,
                                'accion': accion,
                                'isbn': isbn,
                                'id_usuario': id_usuario
                            })

            print("✅ Datos cargados exitosamente!")

        except Exception as e:
            print(f"❌ Error cargando datos: {e}")
            print("📝 Inicializando con datos por defecto...")
            self.inicializar_datos_por_defecto()

    # Métodos de operaciones (se mantienen igual pero con mejoras visuales)
    def añadir_libro(self, titulo, autor, categoria, isbn):
        """Añade un nuevo libro a la biblioteca"""
        if isbn in self.libros:
            print(f"❌ Error: El libro con ISBN {isbn} ya existe.")
            return False

        self.libros[isbn] = Libro(titulo, autor, categoria, isbn)
        print(f"✅ Libro '{titulo}' añadido exitosamente.")
        self.guardar_datos()
        return True

    def quitar_libro(self, isbn):
        """Elimina un libro de la biblioteca"""
        if isbn not in self.libros:
            print(f"❌ Error: No existe un libro con ISBN {isbn}.")
            return False

        libro = self.libros[isbn]
        if not libro.disponible:
            print(f"❌ Error: El libro '{libro.obtener_titulo()}' está prestado y no puede ser eliminado.")
            return False

        del self.libros[isbn]
        print(f"✅ Libro '{libro.obtener_titulo()}' eliminado exitosamente.")
        self.guardar_datos()
        return True

    def registrar_usuario(self, nombre, id_usuario):
        """Registra un nuevo usuario en la biblioteca"""
        if id_usuario in self.ids_usuarios:
            print(f"❌ Error: El ID de usuario {id_usuario} ya está registrado.")
            return False

        nuevo_usuario = Usuario(nombre, id_usuario)
        self.usuarios[id_usuario] = nuevo_usuario
        self.ids_usuarios.add(id_usuario)
        print(f"✅ Usuario '{nombre}' registrado exitosamente con ID {id_usuario}.")
        self.guardar_datos()
        return True

    def dar_de_baja_usuario(self, id_usuario):
        """Da de baja a un usuario de la biblioteca"""
        if id_usuario not in self.ids_usuarios:
            print(f"❌ Error: No existe un usuario con ID {id_usuario}.")
            return False

        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(
                f"❌ Error: El usuario tiene {len(usuario.libros_prestados)} libros prestados y no puede ser dado de baja.")
            return False

        del self.usuarios[id_usuario]
        self.ids_usuarios.remove(id_usuario)
        print(f"✅ Usuario '{usuario.nombre}' dado de baja exitosamente.")
        self.guardar_datos()
        return True

    def prestar_libro(self, isbn, id_usuario):
        """Presta un libro a un usuario"""
        if isbn not in self.libros:
            print(f"❌ Error: No existe un libro con ISBN {isbn}.")
            return False

        if id_usuario not in self.ids_usuarios:
            print(f"❌ Error: No existe un usuario con ID {id_usuario}.")
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if not libro.disponible:
            print(f"❌ Error: El libro '{libro.obtener_titulo()}' no está disponible.")
            return False

        # Realizar el préstamo
        usuario.tomar_prestado(libro)

        # Registrar en el historial
        self.historial_prestamos.append({
            'accion': 'préstamo',
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'isbn': isbn,
            'id_usuario': id_usuario
        })

        print(f"✅ Libro '{libro.obtener_titulo()}' prestado a {usuario.nombre} exitosamente.")
        self.guardar_datos()
        return True

    def devolver_libro(self, isbn, id_usuario):
        """Devuelve un libro prestado por un usuario"""
        if isbn not in self.libros:
            print(f"❌ Error: No existe un libro con ISBN {isbn}.")
            return False

        if id_usuario not in self.ids_usuarios:
            print(f"❌ Error: No existe un usuario con ID {id_usuario}.")
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        if libro not in usuario.libros_prestados:
            print(f"❌ Error: El usuario {usuario.nombre} no tiene prestado el libro '{libro.obtener_titulo()}'.")
            return False

        # Realizar la devolución
        usuario.devolver(libro)

        # Registrar en el historial
        self.historial_prestamos.append({
            'accion': 'devolución',
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'isbn': isbn,
            'id_usuario': id_usuario
        })

        print(f"✅ Libro '{libro.obtener_titulo()}' devuelto por {usuario.nombre} exitosamente.")
        self.guardar_datos()
        return True

    def buscar_libros(self, criterio, valor):
        """Busca libros por título, autor o categoría"""
        resultados = []
        valor = valor.lower()

        for libro in self.libros.values():
            if criterio.lower() == 'titulo' and valor in libro.obtener_titulo().lower():
                resultados.append(libro)
            elif criterio.lower() == 'autor' and valor in libro.obtener_autor().lower():
                resultados.append(libro)
            elif criterio.lower() == 'categoria' and valor in libro.categoria.lower():
                resultados.append(libro)

        return resultados

    def listar_libros_prestados_usuario(self, id_usuario):
        """Lista todos los libros prestados a un usuario específico"""
        if id_usuario not in self.ids_usuarios:
            print(f"❌ Error: No existe un usuario con ID {id_usuario}.")
            return None

        usuario = self.usuarios[id_usuario]
        return usuario.listar_libros_prestados()

    def listar_todos_libros(self):
        """Lista todos los libros en la biblioteca"""
        return [libro for libro in self.libros.values()]

    def listar_todos_usuarios(self):
        """Lista todos los usuarios registrados"""
        return [usuario for usuario in self.usuarios.values()]

    def obtener_libro_por_isbn(self, isbn):
        """Obtiene un libro por su ISBN"""
        return self.libros.get(isbn)

    def mostrar_info_usuarios(self):
        """Muestra información detallada de todos los usuarios"""
        print("\n👥 INFORMACIÓN DE USUARIOS REGISTRADOS:")
        print("-" * 50)
        for i, (id_usuario, usuario) in enumerate(self.usuarios.items(), 1):
            print(f"{i}. {usuario.nombre}")
            print(f"   ID: {id_usuario}")
            print(f"   Libros prestados: {len(usuario.libros_prestados)}")
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(f"     - {libro.obtener_titulo()}")
            print()