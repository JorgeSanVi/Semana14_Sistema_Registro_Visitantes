# Clase que maneja la lógica del registro de visitantes
class VisitaServicio:
    # Constructor que inicializa la lista privada de visitantes
    def __init__(self):
        self._visitantes = []

    # Método para registrar un nuevo visitante en la lista
    def registrar_visitante(self, visitante):
        self._visitantes.append(visitante)

    # Método para devolver la lista de visitantes registrados
    def obtener_visitantes(self):
        return self._visitantes

    # Método para eliminar un visitante según su posición en la lista
    def eliminar_visitante(self, indice):
        if 0 <= indice < len(self._visitantes):
            del self._visitantes[indice]