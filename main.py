# Importamos la capa de servicio
from servicios.visita_servicio import VisitaServicio

# Importamos la interfaz gráfica
from ui.app_tkinter import AppTkinter


# Función principal que inicia el programa
def main():
    # Creamos el servicio que manejará los visitantes
    servicio = VisitaServicio()

    # Creamos la aplicación y le pasamos el servicio
    app = AppTkinter(servicio)

    # Ejecutamos la ventana principal
    app.ejecutar()


# Verificamos que este archivo sea el punto de inicio
if __name__ == "__main__":
    main()