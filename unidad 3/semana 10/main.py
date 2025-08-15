from inventario import Inventario
from producto import Producto
import os

def menu():
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Mostrar productos")
    print("2. Añadir producto")
    print("3. Eliminar producto")
    print("4. Actualizar producto")
    print("5. Buscar producto")
    print("6. Salir")
    return input("Seleccione una opción: ")


def main():
    archivo = "inventario.txt"
    inventario = Inventario(archivo=archivo)

    # Aviso de origen de los datos
    if not os.path.exists(archivo):
        print(" Se cargaron datos de ejemplo y se creó el archivo inventario.txt")
    else:
        print("Datos cargados desde el archivo inventario.txt")

    while True:
        opcion = menu()

        if opcion == "1":
            inventario.mostrar_productos()

        elif opcion == "2":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido exitosamente.")

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "4":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            nueva_cantidad = int(cantidad) if cantidad else None
            nuevo_precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "5":
            nombre = input("Ingrese nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "6":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
