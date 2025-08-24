from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()  # Carga JSON si existe

    while True:
        print("\n---  SISTEMA DE INVENTARIO - TIENDA DE CELULARES ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Mostrar valor total del inventario")
        print("7. Guardar y salir")
        opcion = input(" Elige una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print(" No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print(f" Valor total del inventario: ${inventario.valor_total_inventario():.2f}")

        elif opcion == "7":
            # Guardar JSON y CSV automáticamente
            inventario.guardar_en_archivo()
            inventario.exportar_csv()
            print(" Inventario guardado en JSON y CSV. Saliendo del sistema...")
            break

        else:
            print(" Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
