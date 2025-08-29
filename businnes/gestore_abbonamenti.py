import datetime

from domain.attività.contratto_abbonamento import ContrattoAbbonamento
from domain.servizio.abbonamento import Abbonamento

from businnes.gestore_atleti import GestoreAtleti

class GestoreAbbonamenti:

    def __init__(self):
        self._lista_abbonamenti= {}
        self._lista_contratti= {}

        self._gestore_atleti = None

    def get_lista_abbonamenti(self):
        lista_abbonamenti = []

        for id_abbonamento in self._lista_abbonamenti.keys():
            lista_abbonamenti.append(self._lista_abbonamenti[id_abbonamento])

        return lista_abbonamenti

    def get_lista_contratti(self):
        lista_contratti = []

        for id_contratto in self._lista_contratti.keys():
            lista_contratti.append(self._lista_contratti[id_contratto])

        return lista_contratti

    def get_abbonamento(self, id_abbonamento: int):
        return self._lista_abbonamenti[id_abbonamento]

    def get_contratto_per_id(self, id_contratto: int):
        return self._lista_contratti[id_contratto]

    def get_contratto_atleta(self, id_atleta: int):
        for id_contratto in self._lista_contratti.keys():
            if id_atleta == self._lista_contratti[id_contratto].get_atleta():
                return self._lista_contratti[id_contratto]
        return None

    def controllo_scadenze(self):
        abbonamenti_in_scadenza = []

        for id_contratto in self._lista_contratti.keys():
            if (datetime.date.today() + datetime.timedelta(days=-1)) == self._lista_contratti[id_contratto].get_scadenza(): #Se l'abbonamento scade domani
                abbonamenti_in_scadenza.append(self._lista_contratti[id_contratto])

        if not abbonamenti_in_scadenza:
            return None

        return abbonamenti_in_scadenza

    def controllo_tipo_abbonamento(self, id_contratto: int, tipo: str):
        contratto_abbonamento = self._lista_contratti[id_contratto]

        if contratto_abbonamento.get_tipologia() == tipo:
            return True
        return False

    def controllo_abbonamento_scaduto(self, id_contratto: int):
        contratto_abbonamento = self._lista_contratti[id_contratto]

        if datetime.date.today() >= contratto_abbonamento.get_scadenza():
            return True

        return False

    def set_gestori(self, gestore_atleti: GestoreAtleti):
        self._gestore_atleti = gestore_atleti

    def set_lista_abbonamenti(self, lista_abbonamenti: list[Abbonamento]):
        for abbonamento in lista_abbonamenti:
            if abbonamento.get_id() not in self._lista_abbonamenti.keys():
                self._lista_abbonamenti.update({abbonamento.get_id(): abbonamento})

    def set_lista_contratti(self, lista_contratti: list[ContrattoAbbonamento]):
        for contratto in lista_contratti:
            if contratto.get_id() not in self._lista_contratti.keys():
                self._lista_contratti.update({contratto.get_id(): contratto})
                self._gestore_atleti.get_atleta_per_id(contratto.get_atleta()).assegna_abbonamento(contratto.get_id())

    def crea_contratto(self, id_atleta: int, id_abbonamento: int):
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)
        abbonamento = self._lista_abbonamenti[id_abbonamento]

        if abbonamento is None or atleta is None:
            return False

        for id_contratto in self._lista_contratti.keys():
            contratto = self._lista_contratti[id_contratto]
            if contratto.get_atleta() == id_atleta and contratto.get_abbonamento() == id_abbonamento:
                return False

        abbonamento = self._lista_abbonamenti[id_abbonamento]
        nuovo_contratto = ContrattoAbbonamento(id_atleta, id_abbonamento, abbonamento.get_durata(), abbonamento.get_tipo(), datetime.date.today())

        self._lista_contratti.update({nuovo_contratto.get_id(): nuovo_contratto})
        atleta.assegna_abbonamento(nuovo_contratto.get_id())
        return True

    def crea_abbonamento(self, durata: int, tipologia: str):
        nome_nuovo_abbonamento = f"{durata}-{tipologia}"

        for id_abbonamento in self._lista_abbonamenti.keys():
            if nome_nuovo_abbonamento == self.get_abbonamento(id_abbonamento).get_nome():
                return False

        nuovo_abbonamento = Abbonamento(durata, tipologia)
        self._lista_abbonamenti.update({nuovo_abbonamento.get_id(): nuovo_abbonamento})

        return True