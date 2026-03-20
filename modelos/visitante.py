# Importamos dataclass para crear una clase de datos de forma sencilla
from dataclasses import dataclass


# Esta clase representa a un visitante del sistema
@dataclass
class Visitante:
    # Cédula del visitante
    cedula: str

    # Nombre completo del visitante
    nombre_completo: str

    # Motivo por el que realiza la visita
    motivo_visita: str