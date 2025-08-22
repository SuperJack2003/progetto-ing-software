from domain.attività.atleta import Atleta
from domain.attività.contratto_abbonamento import ContrattoAbbonamento
from domain.servizio.abbonamento import Abbonamento

class GestoreAbbonamenti:

    def __init__(self):
        self._lista_abbonamenti= []
        self._lista_contratti= []

    def get_lista_abbonamenti(self):
        return self._lista_abbonamenti

    def get_lista_contratti(self):
        return self._lista_contratti

    def get_abbonamento(self, nome):
        for abbonamento in self._lista_abbonamenti:
            if abbonamento.get_nome() == nome:
                return abbonamento
        return None

    def get_contratto(self, atleta: Atleta):
        for contratto in self._lista_contratti:
            if contratto.get_atleta() == atleta:
                return contratto
        return None

    def set_lista_abbonamenti(self, lista_abbonamenti):
        self._lista_abbonamenti = lista_abbonamenti

    def set_lista_contratti(self, lista_contratti):
        self._lista_contratti = lista_contratti

    #def aggiungi_contratto(self, atleta: Atleta, abbonamento: Abbonamento):
    #    for contratto in self._lista_contratti:
    #        if contratto.get_atleta() == atleta:
