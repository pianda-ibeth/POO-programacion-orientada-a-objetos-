import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import json
import os


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Mi Agenda Personal Mensual ✨")
        self.root.geometry("1100x750")
        self.root.resizable(True, True)
        self.root.configure(bg='#f0f8ff')  # Azul claro muy suave

        # Configurar estilo con colores pasteles
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Configurar colores pasteles
        self.style.configure('TFrame', background='#f0f8ff')
        self.style.configure('TLabel', background='#f0f8ff', foreground='#5a5a5a', font=('Arial', 10))
        self.style.configure('Title.TLabel', background='#f0f8ff', foreground='#6a5acd', font=('Arial', 18, 'bold'))
        self.style.configure('TButton', font=('Arial', 10), background='#b0e0e6')
        self.style.map('TButton', background=[('active', '#87ceeb')])
        self.style.configure('Accent.TButton', font=('Arial', 10, 'bold'), background='#ffb6c1')
        self.style.map('Accent.TButton', background=[('active', '#ffc0cb')])
        self.style.configure('Green.TButton', font=('Arial', 10), background='#98fb98')
        self.style.map('Green.TButton', background=[('active', '#90ee90')])
        self.style.configure('Treeview', background='#f5f5f5', fieldbackground='#f5f5f5', foreground='#333333')
        self.style.configure('Treeview.Heading', background='#d8bfd8', foreground='#4b0082', font=('Arial', 10, 'bold'))
        self.style.configure('TLabelframe', background='#f0f8ff', foreground='#6a5acd')
        self.style.configure('TLabelframe.Label', background='#f0f8ff', foreground='#6a5acd',
                             font=('Arial', 11, 'bold'))

        # Datos de ejemplo para tu agenda mensual
        self.eventos_muestras = [
            {"fecha": datetime.now().strftime("%d/%m/%Y"), "hora": "10:00",
             "descripcion": "Ir al médico - chequeo general", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=3)).strftime("%d/%m/%Y"), "hora": "16:30",
             "descripcion": "Comprar pastillas para la alergia", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=5)).strftime("%d/%m/%Y"), "hora": "11:00",
             "descripcion": "Comprar cremas faciales", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y"), "hora": "20:00",
             "descripcion": "Salir con amigos - cine", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=10)).strftime("%d/%m/%Y"), "hora": "14:00",
             "descripcion": "Presentar práctico experimental de programación", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=15)).strftime("%d/%m/%Y"), "hora": "09:00",
             "descripcion": "Evaluación mensual de matemáticas", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=18)).strftime("%d/%m/%Y"), "hora": "17:00",
             "descripcion": "Tarea de inglés - essay writing", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=22)).strftime("%d/%m/%Y"), "hora": "15:00",
             "descripcion": "Ir al médico - control de tratamiento", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=25)).strftime("%d/%m/%Y"), "hora": "12:00",
             "descripcion": "Comprar vitaminas y suplementos", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=28)).strftime("%d/%m/%Y"), "hora": "18:30",
             "descripcion": "Cumpleaños de mi hermana - fiesta sorpresa", "completado": False},
            {"fecha": (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y"), "hora": "10:30",
             "descripcion": "Ir al médico - resultados de análisis", "completado": False}
        ]

        self.eventos = []
        self.cargar_eventos()

        # Si no hay eventos, cargar las muestras
        if not self.eventos:
            self.eventos = self.eventos_muestras
            self.guardar_eventos()

        self.crear_interfaz()
        self.actualizar_lista_eventos()
        self.actualizar_estadisticas()

    def crear_interfaz(self):
        # Frame principal con degradado
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar grid para expansión
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Título con emojis y estilo mejorado
        titulo_frame = ttk.Frame(main_frame)
        titulo_frame.grid(row=0, column=0, columnspan=3, pady=(0, 15), sticky=(tk.W, tk.E))
        titulo_frame.columnconfigure(0, weight=1)

        titulo = ttk.Label(titulo_frame, text="📅 Mi Agenda Personal Mensual ✨", style='Title.TLabel')
        titulo.grid(row=0, column=0)

        # Frame para estadísticas
        stats_frame = ttk.Frame(main_frame)
        stats_frame.grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky=(tk.W, tk.E))

        self.total_var = tk.StringVar(value="Total: 0")
        self.completados_var = tk.StringVar(value="Completados: 0")
        self.pendientes_var = tk.StringVar(value="Pendientes: 0")

        ttk.Label(stats_frame, textvariable=self.total_var, font=('Arial', 10, 'bold'),
                  foreground='#6a5acd').pack(side=tk.LEFT, padx=(0, 20))
        ttk.Label(stats_frame, textvariable=self.completados_var, font=('Arial', 10, 'bold'),
                  foreground='#2e8b57').pack(side=tk.LEFT, padx=(0, 20))
        ttk.Label(stats_frame, textvariable=self.pendientes_var, font=('Arial', 10, 'bold'),
                  foreground='#dc143c').pack(side=tk.LEFT)

        # Frame para entrada de datos con color pastel
        input_frame = ttk.LabelFrame(main_frame, text="➕ Nuevo Evento", padding="10")
        input_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N), padx=(0, 10), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)

        # Fecha
        ttk.Label(input_frame, text="📅 Fecha (dd/mm/aaaa):", font=('Arial', 10, 'bold')).grid(row=0, column=0,
                                                                                              sticky=tk.W, pady=5)
        self.fecha_var = tk.StringVar()
        fecha_entry = ttk.Entry(input_frame, textvariable=self.fecha_var, width=15, font=('Arial', 10))
        fecha_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(5, 0))

        # Botón para fecha de hoy
        ttk.Button(input_frame, text="Hoy",
                   command=self.establecer_fecha_hoy, style='TButton').grid(row=0, column=2, padx=(5, 0))

        # Hora
        ttk.Label(input_frame, text="⏰ Hora (hh:mm):", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W,
                                                                                        pady=5)
        self.hora_var = tk.StringVar()
        hora_entry = ttk.Entry(input_frame, textvariable=self.hora_var, width=8, font=('Arial', 10))
        hora_entry.grid(row=1, column=1, sticky=tk.W, pady=5, padx=(5, 0))

        # Botón para hora actual
        ttk.Button(input_frame, text="Ahora",
                   command=self.establecer_hora_ahora, style='TButton').grid(row=1, column=2, padx=(5, 0))

        # Descripción
        ttk.Label(input_frame, text="📝 Descripción:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky=tk.W,
                                                                                       pady=5)
        self.descripcion_var = tk.StringVar()
        descripcion_entry = ttk.Entry(input_frame, textvariable=self.descripcion_var, width=30, font=('Arial', 10))
        descripcion_entry.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=(5, 0))

        # Botones de acción
        botones_frame = ttk.Frame(input_frame)
        botones_frame.grid(row=3, column=0, columnspan=3, pady=15)

        ttk.Button(botones_frame, text="✅ Agregar Evento",
                   command=self.agregar_evento, style='Accent.TButton').pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(botones_frame, text="❌ Eliminar Evento",
                   command=self.eliminar_evento, style='Accent.TButton').pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(botones_frame, text="✓ Marcar como Completado",
                   command=self.marcar_completado, style='Green.TButton').pack(side=tk.LEFT)

        # Frame para la lista de eventos
        lista_frame = ttk.LabelFrame(main_frame, text="🗓️ Eventos Programados", padding="10")
        lista_frame.grid(row=2, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        lista_frame.columnconfigure(0, weight=1)
        lista_frame.rowconfigure(0, weight=1)

        # Treeview para mostrar eventos
        columnas = ('completado', 'fecha', 'hora', 'descripcion')
        self.tree = ttk.Treeview(lista_frame, columns=columnas, show='headings', height=18)

        # Definir encabezados
        self.tree.heading('completado', text='✓')
        self.tree.heading('fecha', text='📅 Fecha')
        self.tree.heading('hora', text='⏰ Hora')
        self.tree.heading('descripcion', text='📝 Descripción')

        # Definir anchos de columna
        self.tree.column('completado', width=40, anchor=tk.CENTER)
        self.tree.column('fecha', width=100, anchor=tk.CENTER)
        self.tree.column('hora', width=80, anchor=tk.CENTER)
        self.tree.column('descripcion', width=350)

        # Scrollbar para el treeview
        scrollbar = ttk.Scrollbar(lista_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Frame para botones inferiores
        footer_frame = ttk.Frame(main_frame)
        footer_frame.grid(row=3, column=0, columnspan=2, pady=20)
        footer_frame.columnconfigure(0, weight=1)
        footer_frame.columnconfigure(1, weight=1)
        footer_frame.columnconfigure(2, weight=1)
        footer_frame.columnconfigure(3, weight=1)

        ttk.Button(footer_frame, text="🧹 Limpiar Campos",
                   command=self.limpiar_campos, style='TButton').grid(row=0, column=0, padx=5)
        ttk.Button(footer_frame, text="💾 Guardar Cambios",
                   command=self.guardar_eventos, style='TButton').grid(row=0, column=1, padx=5)
        ttk.Button(footer_frame, text="📊 Ver Estadísticas",
                   command=self.mostrar_estadisticas, style='TButton').grid(row=0, column=2, padx=5)
        ttk.Button(footer_frame, text="🚪 Salir",
                   command=self.root.quit, style='Accent.TButton').grid(row=0, column=3, padx=5)

        # Información de formato
        info_frame = ttk.Frame(main_frame)
        info_frame.grid(row=4, column=0, columnspan=2, pady=(10, 0))

        ttk.Label(info_frame, text="💡 Formato fecha: dd/mm/aaaa (ej: 15/12/2023)",
                  font=("Arial", 9), foreground="#6a5acd").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Label(info_frame, text="💡 Formato hora: hh:mm (24h) (ej: 14:30)",
                  font=("Arial", 9), foreground="#6a5acd").pack(side=tk.LEFT)

    def establecer_fecha_hoy(self):
        self.fecha_var.set(datetime.now().strftime("%d/%m/%Y"))

    def establecer_hora_ahora(self):
        self.hora_var.set(datetime.now().strftime("%H:%M"))

    def agregar_evento(self):
        fecha = self.fecha_var.get().strip()
        hora = self.hora_var.get().strip()
        descripcion = self.descripcion_var.get().strip()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        # Validar formato de fecha (dd/mm/yyyy)
        try:
            datetime.strptime(fecha, '%d/%m/%Y')
        except ValueError:
            messagebox.showwarning("Formato incorrecto", "La fecha debe tener el formato dd/mm/aaaa.")
            return

        # Validar formato de hora (hh:mm)
        try:
            datetime.strptime(hora, '%H:%M')
        except ValueError:
            messagebox.showwarning("Formato incorrecto", "La hora debe tener el formato hh:mm (24 horas).")
            return

        nuevo_evento = {
            "fecha": fecha,
            "hora": hora,
            "descripcion": descripcion,
            "completado": False
        }

        self.eventos.append(nuevo_evento)
        self.guardar_eventos()
        self.actualizar_lista_eventos()
        self.actualizar_estadisticas()
        self.limpiar_campos()

        messagebox.showinfo("Éxito", "✅ Evento agregado correctamente.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección vacía", "Por favor, seleccione un evento para eliminar.")
            return

        # Obtener detalles del evento seleccionado
        item = seleccion[0]
        valores = self.tree.item(item, 'values')

        # Confirmar eliminación
        if messagebox.askyesno("Confirmar eliminación",
                               f"¿Está seguro de que desea eliminar el evento?\n\n"
                               f"Fecha: {valores[1]}\n"
                               f"Hora: {valores[2]}\n"
                               f"Descripción: {valores[3]}"):
            index = self.tree.index(item)
            del self.eventos[index]
            self.guardar_eventos()
            self.actualizar_lista_eventos()
            self.actualizar_estadisticas()
            messagebox.showinfo("Eliminado", "❌ Evento eliminado correctamente.")

    def marcar_completado(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección vacía", "Por favor, seleccione un evento para marcar como completado.")
            return

        item = seleccion[0]
        index = self.tree.index(item)

        # Cambiar estado de completado
        self.eventos[index]["completado"] = not self.eventos[index]["completado"]

        self.guardar_eventos()
        self.actualizar_lista_eventos()
        self.actualizar_estadisticas()

        estado = "completado" if self.eventos[index]["completado"] else "pendiente"
        messagebox.showinfo("Estado actualizado", f"✅ Evento marcado como {estado}.")

    def actualizar_lista_eventos(self):
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ordenar eventos por fecha y hora
        eventos_ordenados = sorted(self.eventos, key=lambda x: (
            datetime.strptime(x['fecha'], '%d/%m/%Y'),
            datetime.strptime(x['hora'], '%H:%M')
        ))

        # Agregar eventos al treeview
        for i, evento in enumerate(eventos_ordenados):
            completado = "✓" if evento["completado"] else ""
            tag = 'completado' if evento["completado"] else 'pendiente'
            self.tree.insert('', tk.END, values=(
                completado,
                evento['fecha'],
                evento['hora'],
                evento['descripcion']
            ), tags=(tag,))

        # Configurar colores para eventos completados y pendientes
        self.tree.tag_configure('completado', background='#e6ffe6',
                                foreground='#006400')  # Verde claro para completados
        self.tree.tag_configure('pendiente', background='#fff0f5', foreground='#8b0000')  # Rosa claro para pendientes

    def actualizar_estadisticas(self):
        total = len(self.eventos)
        completados = sum(1 for evento in self.eventos if evento["completado"])
        pendientes = total - completados

        self.total_var.set(f"Total: {total}")
        self.completados_var.set(f"Completados: {completados}")
        self.pendientes_var.set(f"Pendientes: {pendientes}")

    def mostrar_estadisticas(self):
        total = len(self.eventos)
        completados = sum(1 for evento in self.eventos if evento["completado"])
        pendientes = total - completados
        porcentaje = (completados / total * 100) if total > 0 else 0

        messagebox.showinfo("Estadísticas",
                            f"📊 Resumen de tu agenda:\n\n"
                            f"• Total de eventos: {total}\n"
                            f"• Eventos completados: {completados}\n"
                            f"• Eventos pendientes: {pendientes}\n"
                            f"• Progreso: {porcentaje:.1f}% completado")

    def limpiar_campos(self):
        self.fecha_var.set("")
        self.hora_var.set("")
        self.descripcion_var.set("")

    def guardar_eventos(self):
        try:
            with open('agenda_eventos.json', 'w', encoding='utf-8') as f:
                json.dump(self.eventos, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("Guardado", "💾 Eventos guardados correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los eventos: {str(e)}")

    def cargar_eventos(self):
        if os.path.exists('agenda_eventos.json'):
            try:
                with open('agenda_eventos.json', 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    # Asegurarse de que todos los eventos tengan el campo 'completado'
                    for evento in datos:
                        if 'completado' not in evento:
                            evento['completado'] = False
                    self.eventos = datos
            except:
                self.eventos = []


def main():
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()


if __name__ == "__main__":
    main()