import datetime

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

    def controllo_scadenze(self):
        abbonamenti_in_scadenza = []

        for contratto in self._lista_contratti:
            if (datetime.date.today() + datetime.timedelta(days=-1)) == contratto.get_scadenza(): #Se l'abbonamento scade domani
                abbonamenti_in_scadenza.append(contratto)

        if not abbonamenti_in_scadenza:
            return None

        return abbonamenti_in_scadenza

    def controllo_tipo_abbonamento(self, nome_abbonamento: str, tipo: str):
        abbonamento = self.get_abbonamento(nome_abbonamento)
        if abbonamento.get_tipo() == tipo:
            return True
        return False

    def controllo_abbonamento_scaduto(self, nome_abbonamento: str):
        abbonamento = self.get_abbonamento(nome_abbonamento)

        if datetime.date.today() >= abbonamento.get_scadenza():
            return True

        return False

    def set_lista_abbonamenti(self, lista_abbonamenti):
        self._lista_abbonamenti = lista_abbonamenti

    def set_lista_contratti(self, lista_contratti):
        self._lista_contratti = lista_contratti

    def aggiungi_contratto(self, atleta: Atleta, abbonamento: Abbonamento):
        for contratto in self._lista_contratti:
            if contratto.get_atleta() == atleta:
                self._lista_contratti.remove(contratto)

        nuovo_contratto = ContrattoAbbonamento(atleta, abbonamento, datetime.date.today().__str__())
        self._lista_contratti.append(nuovo_contratto)
        atleta.assegna_abbonamento(nuovo_contratto)

        return True

    def aggiungi_abbonamento(self, durata: int, tipologia: str):
        nuovo_abbonamento = f"{durata}-{tipologia}"
        for abbonamento in self._lista_abbonamenti:
            if abbonamento.get_nome() == nuovo_abbonamento:
                return False

        abbonamento = Abbonamento(durata, tipologia)
        self._lista_abbonamenti.append(abbonamento)

        return True