# Importamos tkinter para crear la interfaz gráfica
import tkinter as tk

# Importamos ttk para la tabla y messagebox para mostrar mensajes
from tkinter import ttk, messagebox

# Importamos la clase Visitante desde la capa modelo
from modelos.visitante import Visitante


# Clase principal de la interfaz gráfica
class AppTkinter:
    # Constructor que recibe el servicio por inyección de dependencias
    def __init__(self, servicio):
        self.servicio = servicio

        # Creamos la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Registro de Visitantes")
        self.ventana.geometry("700x450")
        self.ventana.resizable(False, False)

        # Llamamos al método que construye la interfaz
        self.crear_componentes()

    # Método para crear todos los componentes de la ventana
    def crear_componentes(self):
        # Título principal
        titulo = tk.Label(
            self.ventana,
            text="Registro de Visitantes",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        # Frame para el formulario de entrada
        frame_formulario = tk.Frame(self.ventana)
        frame_formulario.pack(pady=10)

        # Etiqueta y campo para la cédula
        tk.Label(frame_formulario, text="Cédula:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_cedula = tk.Entry(frame_formulario, width=30)
        self.entry_cedula.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo para el nombre completo
        tk.Label(frame_formulario, text="Nombre completo:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_formulario, width=30)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y campo para el motivo de visita
        tk.Label(frame_formulario, text="Motivo de visita:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_motivo = tk.Entry(frame_formulario, width=30)
        self.entry_motivo.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones de acción
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        # Botón para registrar visitantes
        btn_registrar = tk.Button(
            frame_botones,
            text="Registrar",
            command=self.registrar_visitante,
            width=15
        )
        btn_registrar.grid(row=0, column=0, padx=5)

        # Botón para eliminar un visitante seleccionado
        btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            command=self.eliminar_visitante,
            width=15
        )
        btn_eliminar.grid(row=0, column=1, padx=5)

        # Botón para limpiar los campos del formulario
        btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar Campos",
            command=self.limpiar_campos,
            width=15
        )
        btn_limpiar.grid(row=0, column=2, padx=5)

        # Creamos la tabla para mostrar los visitantes registrados
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("Cedula", "Nombre", "Motivo"),
            show="headings",
            height=10
        )

        # Encabezados de la tabla
        self.tabla.heading("Cedula", text="Cédula")
        self.tabla.heading("Nombre", text="Nombre Completo")
        self.tabla.heading("Motivo", text="Motivo de Visita")

        # Ancho de cada columna
        self.tabla.column("Cedula", width=150)
        self.tabla.column("Nombre", width=220)
        self.tabla.column("Motivo", width=220)

        # Mostramos la tabla en la ventana
        self.tabla.pack(pady=10)

    # Método para registrar un visitante nuevo
    def registrar_visitante(self):
        # Obtenemos los datos escritos por el usuario
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()
        motivo = self.entry_motivo.get().strip()

        # Validamos que no existan campos vacíos
        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        # Creamos un objeto Visitante con los datos ingresados
        visitante = Visitante(cedula, nombre, motivo)

        # Enviamos el visitante al servicio para guardarlo
        self.servicio.registrar_visitante(visitante)

        # Actualizamos la tabla y limpiamos los campos
        self.actualizar_tabla()
        self.limpiar_campos()

        # Mostramos mensaje de éxito
        messagebox.showinfo("Éxito", "Visitante registrado correctamente.")

    # Método para recargar la tabla con los datos actuales
    def actualizar_tabla(self):
        # Eliminamos las filas actuales de la tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # Insertamos nuevamente todos los visitantes guardados
        for i, visitante in enumerate(self.servicio.obtener_visitantes()):
            self.tabla.insert(
                "",
                "end",
                iid=i,
                values=(visitante.cedula, visitante.nombre_completo, visitante.motivo_visita)
            )

    # Método para eliminar el visitante seleccionado en la tabla
    def eliminar_visitante(self):
        # Obtenemos la fila seleccionada
        seleccion = self.tabla.selection()

        # Validamos que exista una selección
        if not seleccion:
            messagebox.showwarning("Sin selección", "Seleccione un visitante para eliminar.")
            return

        # Convertimos el identificador seleccionado en índice
        indice = int(seleccion[0])

        # Eliminamos el visitante desde el servicio
        self.servicio.eliminar_visitante(indice)

        # Actualizamos la tabla y limpiamos campos
        self.actualizar_tabla()
        self.limpiar_campos()

        # Mostramos mensaje de éxito
        messagebox.showinfo("Éxito", "Visitante eliminado correctamente.")

    # Método para vaciar los campos del formulario
    def limpiar_campos(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    # Método que ejecuta el ciclo principal de la app
    def ejecutar(self):
        self.ventana.mainloop()