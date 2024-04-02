# feito por Dayvsson e Douglas

class Evento:
    def __init__(self, titulo, data, hora, local):
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.local = local

    def __str__(self):
        return f"Evento: {self.titulo}\nData: {self.data}\nHora:{self.hora}\nlocal:{self.local}"