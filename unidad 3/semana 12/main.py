from Biblioteca import Biblioteca


def mostrar_menu_principal():
    """Muestra el menú principal de la biblioteca"""
    print("\n" + "=" * 50)
    print("        SISTEMA DE GESTIÓN DE BIBLIOTECA ")
    print("=" * 50)
    print("1.  Gestión de Libros")
    print("2.  Gestión de Usuarios")
    print("3.  Préstamos y Devoluciones")
    print("4.  Búsqueda de Libros")
    print("5.  Listados")
    print("6.  Salir")
    return input("\nSeleccione una opción: ")


def mostrar_menu_libros():
    """Muestra el menú de gestión de libros"""
    print("\n" + "=" * 50)
    print("        GESTIÓN DE LIBROS")
    print("=" * 50)
    print("1. Añadir nuevo libro")
    print("2. Eliminar libro")
    print("3. Volver al menú principal")
    return input("\nSeleccione una opción: ")


def mostrar_menu_usuarios():
    """Muestra el menú de gestión de usuarios"""
    print("\n" + "=" * 50)
    print("        GESTIÓN DE USUARIOS")
    print("=" * 50)
    print("1. Registrar nuevo usuario")
    print("2. Dar de baja usuario")
    print("3. Volver al menú principal")
    return input("\nSeleccione una opción: ")


def mostrar_menu_prestamos():
    """Muestra el menú de préstamos y devoluciones"""
    print("\n" + "=" * 50)
    print("        PRÉSTAMOS Y DEVOLUCIONES")
    print("=" * 50)
    print("1. Prestar libro")
    print("2. Devolver libro")
    print("3. Volver al menú principal")
    return input("\nSeleccione una opción: ")


def mostrar_menu_busqueda():
    """Muestra el menú de búsqueda"""
    print("\n" + "=" * 50)
    print("        BÚSQUEDA DE LIBROS")
    print("=" * 50)
    print("1. Buscar por título")
    print("2. Buscar por autor")
    print("3. Buscar por categoría")
    print("4. Volver al menú principal")
    return input("\nSeleccione una opción: ")

def mostrar_menu_listados():
    """Muestra el menú de listados"""
    print("\n" + "="*50)
    print("       📋 LISTADOS")
    print("="*50)
    print("1. Listar todos los libros")
    print("2. Listar todos los usuarios")
    print("3. Listar libros prestados por usuario")
    print("4. Ver información detallada de usuarios")  # ← NUEVA OPCIÓN
    print("5. Volver al menú principal")
    return input("\nSeleccione una opción: ")


def main():
    """Función principal del sistema de biblioteca"""
    biblioteca = Biblioteca()

    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            # Gestión de Libros
            while True:
                opcion_libros = mostrar_menu_libros()

                if opcion_libros == "1":
                    print("\n AÑADIR NUEVO LIBRO")
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    categoria = input("Categoría: ")
                    isbn = input("ISBN: ")
                    biblioteca.añadir_libro(titulo, autor, categoria, isbn)

                elif opcion_libros == "2":
                    print("\n ELIMINAR LIBRO")
                    isbn = input("ISBN del libro a eliminar: ")
                    biblioteca.quitar_libro(isbn)

                elif opcion_libros == "3":
                    break

                else:
                    print(" Opción no válida. Intente de nuevo.")

        elif opcion == "2":
            # Gestión de Usuarios
            while True:
                opcion_usuarios = mostrar_menu_usuarios()

                if opcion_usuarios == "1":
                    print("\n REGISTRAR NUEVO USUARIO")
                    nombre = input("Nombre: ")
                    id_usuario = input("ID de usuario: ")
                    biblioteca.registrar_usuario(nombre, id_usuario)

                elif opcion_usuarios == "2":
                    print("\n DAR DE BAJA USUARIO")
                    id_usuario = input("ID del usuario: ")
                    biblioteca.dar_de_baja_usuario(id_usuario)

                elif opcion_usuarios == "3":
                    break

                else:
                    print(" Opción no válida. Intente de nuevo.")

        elif opcion == "3":
            # Préstamos y Devoluciones
            while True:
                opcion_prestamos = mostrar_menu_prestamos()

                if opcion_prestamos == "1":
                    print("\n PRESTAR LIBRO")
                    isbn = input("ISBN del libro: ")
                    id_usuario = input("ID del usuario: ")
                    biblioteca.prestar_libro(isbn, id_usuario)

                elif opcion_prestamos == "2":
                    print("\n DEVOLVER LIBRO")
                    isbn = input("ISBN del libro: ")
                    id_usuario = input("ID del usuario: ")
                    biblioteca.devolver_libro(isbn, id_usuario)

                elif opcion_prestamos == "3":
                    break

                else:
                    print(" Opción no válida. Intente de nuevo.")

        elif opcion == "4":
            # Búsqueda de Libros
            while True:
                opcion_busqueda = mostrar_menu_busqueda()

                if opcion_busqueda == "1":
                    print("\n BUSCAR POR TÍTULO")
                    titulo = input("Título a buscar: ")
                    resultados = biblioteca.buscar_libros("titulo", titulo)
                    mostrar_resultados_busqueda(resultados)

                elif opcion_busqueda == "2":
                    print("\n BUSCAR POR AUTOR")
                    autor = input("Autor a buscar: ")
                    resultados = biblioteca.buscar_libros("autor", autor)
                    mostrar_resultados_busqueda(resultados)

                elif opcion_busqueda == "3":
                    print("\n BUSCAR POR CATEGORÍA")
                    categoria = input("Categoría a buscar: ")
                    resultados = biblioteca.buscar_libros("categoria", categoria)
                    mostrar_resultados_busqueda(resultados)

                elif opcion_busqueda == "4":
                    break

                else:
                    print(" Opción no válida. Intente de nuevo.")

        elif opcion == "5":
            # Listados
            while True:
                opcion_listados = mostrar_menu_listados()

                if opcion_listados == "1":
                    print("\n TODOS LOS LIBROS")
                    libros = biblioteca.listar_todos_libros()
                    for i, libro in enumerate(libros, 1):
                        print(f"{i}. {libro}")

                elif opcion_listados == "2":
                    print("\n TODOS LOS USUARIOS")
                    usuarios = biblioteca.listar_todos_usuarios()
                    for i, usuario in enumerate(usuarios, 1):
                        print(f"{i}. {usuario}")

                elif opcion_listados == "3":
                    print("\n LIBROS PRESTADOS POR USUARIO")
                    id_usuario = input("ID del usuario: ")
                    libros = biblioteca.listar_libros_prestados_usuario(id_usuario)
                    if libros:
                        print(f"\nLibros prestados:")
                        for i, libro in enumerate(libros, 1):
                            print(f"{i}. {libro}")
                    else:
                        print(" No se encontraron libros prestados o el usuario no existe.")

                elif opcion_listados == "4":
                    break

                else:
                    print(" Opción no válida. Intente de nuevo.")

        elif opcion == "6":
            print("\n¡Gracias por usar el sistema de biblioteca digital! 👋")
            break

        else:
            print(" Opción no válida. Por favor, intente de nuevo.")


def mostrar_resultados_busqueda(resultados):
    """Muestra los resultados de búsqueda"""
    if resultados:
        print(f"\n Se encontraron {len(resultados)} resultados:")
        for i, libro in enumerate(resultados, 1):
            print(f"{i}. {libro}")
    else:
        print(" No se encontraron resultados.")


if __name__ == "__main__":
    main()