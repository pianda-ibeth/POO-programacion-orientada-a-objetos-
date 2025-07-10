import os
import subprocess

# ===========================
# CONFIGURACIÓN PERSONALIZADA
# ===========================
TITULO = " DASHBOARD POO"
ESTUDIANTE = "Estudiante: PIANDA MADELIN"
MATERIA = "Materia: Programación Orientada a Objetos"
SEPARADOR = "=" * 60

# ===========================
# FUNCIONES
# ===========================

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n Código de: {ruta_script}\n" + "-" * 50)
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(" El archivo no se encontró.")
        return None
    except Exception as e:
        print(f" Error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f" Error al ejecutar el código: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print(f"\n{SEPARADOR}\n{TITULO}\n{ESTUDIANTE} | {MATERIA}\n{SEPARADOR}")
        for key, val in unidades.items():
            print(f"{key} - {val}")
        print("3 -  Buscar script por nombre")
        print("0 -  Salir")

        opcion = input(" Elige una opción: ")
        if opcion == '0':
            print(" ¡Gracias por usar el dashboard!")
            break
        elif opcion in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[opcion])
            if os.path.exists(ruta_unidad):
                mostrar_sub_menu(ruta_unidad)
            else:
                print("️ La carpeta de unidad no existe.")
        elif opcion == '3':
            buscar_script(ruta_base)
        else:
            print(" Opción no válida.")

def mostrar_sub_menu(ruta_unidad):
    if not os.path.exists(ruta_unidad):
        print(" La ruta de la unidad no existe.")
        return

    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
    if not sub_carpetas:
        print(" No hay subcarpetas en esta unidad.")
        return

    while True:
        print("\n Subtemas disponibles:")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 -  Volver al menú anterior")

        opcion = input(" Elige un subtema: ")
        if opcion == '0':
            break
        try:
            idx = int(opcion) - 1
            if 0 <= idx < len(sub_carpetas):
                ruta_sub = os.path.join(ruta_unidad, sub_carpetas[idx])
                mostrar_scripts(ruta_sub)
            else:
                print(" Opción fuera de rango.")
        except ValueError:
            print(" Entrada inválida.")

def mostrar_scripts(ruta_sub_carpeta):
    if not os.path.exists(ruta_sub_carpeta):
        print(" La carpeta del tema no existe.")
        return

    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
    if not scripts:
        print(" No hay scripts .py en esta carpeta.")
        return

    while True:
        print("\n Scripts disponibles:")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Volver")
        print("9 -  Menú principal")

        opcion = input(" Elige un script: ")
        if opcion == '0':
            break
        elif opcion == '9':
            return
        try:
            idx = int(opcion) - 1
            if 0 <= idx < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[idx])
                codigo = mostrar_codigo(ruta_script)
                if codigo:
                    ejecutar = input(" ¿Ejecutar este script? (1 = Sí / 0 = No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    input(" Presiona Enter para continuar...")
            else:
                print(" Número fuera de rango.")
        except ValueError:
            print(" Entrada inválida.")

def buscar_script(ruta_base):
    nombre = input(" Ingresa parte del nombre del script: ").strip()
    print(f"\n Buscando '{nombre}'...\n" + "-" * 40)
    encontrados = []

    for carpeta_raiz, _, archivos in os.walk(ruta_base):
        for archivo in archivos:
            if archivo.endswith('.py') and nombre.lower() in archivo.lower():
                encontrados.append(os.path.join(carpeta_raiz, archivo))

    if encontrados:
        for idx, path in enumerate(encontrados, 1):
            print(f"{idx}. {path}")
        try:
            eleccion = int(input(" ¿Cuál deseas abrir/ejecutar? (número o 0 para cancelar): "))
            if 1 <= eleccion <= len(encontrados):
                ruta = encontrados[eleccion - 1]
                codigo = mostrar_codigo(ruta)
                if codigo:
                    ejecutar = input(" ¿Ejecutar? (1 = Sí / 0 = No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta)
                    input(" Presiona Enter para volver.")
        except:
            print(" Entrada inválida.")
    else:
        print(" No se encontraron coincidencias.")

# ===========================
# EJECUCIÓN PRINCIPAL
# ===========================
if __name__ == "__main__":
    mostrar_menu()
