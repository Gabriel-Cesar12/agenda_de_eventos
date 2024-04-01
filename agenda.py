#Feito por Brenda e Cesar

class AgendaEventos:
    def __init__(self):
        self.eventos = {}

    def adicionar_evento(self, evento):
        self.eventos.append(evento)

    def editar_evento(self, indice, novo_evento):
        if 0 <= indice < len(self.eventos):
            self.eventos[indice] = novo_evento
            return True
        return False
    
    def remover_evento(self, indice):
        if 0 <= indice < len(self.eventos):
            del self.eventos[indice]
            return True
        return False
    
    def listar_eventos(self):
        for indice, evento in enumerate(self.eventos):
            print("Evento {indice + 1}: ")
            print("Titulo: {evento.titulo}")
            print("Data: {evento.data}")
            print("Hora: {evento.hora}")
            print("Descrição: {evento.descrição}")
            print()