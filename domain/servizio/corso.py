from domain.attività.contratto_allenatore_corso import ContrattoAllenatoreCorso
from domain.attività.contratto_atleta_corso import ContrattoAtletaCorso

class Corso:
    def __init__(self, nome: str, orario_corso: str):
        self._nome = nome
        self._orario_corso = orario_corso
        self._stato = True
        self._lista_iscrizioni = []
        self._contratto_allenatore = None

    def get_lista_iscrizioni(self):
        return self._lista_iscrizioni

    def get_nome(self):
        return self._nome

    def get_orario_corso(self):
        return self._orario_corso

    def get_stato(self):
        return self._stato

    def aggiungi_iscritto(self, iscrizione: ContrattoAtletaCorso):
        self._lista_iscrizioni.append(iscrizione)

    def assegna_allenatore(self, contratto_allenatore: ContrattoAllenatoreCorso):
        self._contratto_allenatore = contratto_allenatore

    def set_status(self, status: bool):
        self._stato = status