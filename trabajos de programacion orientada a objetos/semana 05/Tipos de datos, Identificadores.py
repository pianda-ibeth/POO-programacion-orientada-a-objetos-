# Programa: Registro de Estudiantes
# Descripción:
# Este programa registra información básica de tres estudiantes, incluyendo nombre, edad,
# promedio final y estado de matrícula. Utiliza diferentes tipos de datos como string, int,
# float y boolean. Además, sigue las convenciones de nomenclatura en Python y está comentado
# para facilitar su comprensión. Fue desarrollado usando PyCharm y se publicará en GitHub.

# =====================
# Registro del Estudiante 1
# =====================
nombre_estudiante_1 = "Ana Torres"             # tipo string
edad_estudiante_1 = 20                         # tipo int
promedio_estudiante_1 = 8.7                    # tipo float
matricula_activa_1 = True                      # tipo boolean

# =====================
# Registro del Estudiante 2
# =====================
nombre_estudiante_2 = "Luis Méndez"
edad_estudiante_2 = 22
promedio_estudiante_2 = 6.4
matricula_activa_2 = False

# =====================
# Registro del Estudiante 3
# =====================
nombre_estudiante_3 = "María López"
edad_estudiante_3 = 19
promedio_estudiante_3 = 9.2
matricula_activa_3 = True

# =====================
# Función para mostrar la información de un estudiante
# =====================
def mostrar_estudiante(nombre, edad, promedio, matricula_activa):
    print("Nombre:", nombre)
    print("Edad:", edad, "años")
    print("Promedio Final:", promedio)
    print("¿Matrícula activa?:", matricula_activa)
    print("------------------------")

# =====================
# Llamadas a la función para mostrar la información
# =====================
print("=== REGISTRO DE ESTUDIANTES ===")
mostrar_estudiante(nombre_estudiante_1, edad_estudiante_1, promedio_estudiante_1, matricula_activa_1)
mostrar_estudiante(nombre_estudiante_2, edad_estudiante_2, promedio_estudiante_2, matricula_activa_2)
mostrar_estudiante(nombre_estudiante_3, edad_estudiante_3, promedio_estudiante_3, matricula_activa_3)

