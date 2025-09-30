import datetime
from typing import Optional

from domain.attività.contratto_abbonamento import ContrattoAbbonamento
from domain.servizio.abbonamento import Abbonamento

from businnes.gestore_atleti import GestoreAtleti

class GestoreAbbonamenti:

    def __init__(self, gestore_atleti: GestoreAtleti):
        self._abbonamenti_per_id= {}
        self._contratti_per_id= {}

        self._gestore_atleti = gestore_atleti

    def get_lista_abbonamenti(self):
        return list(self._abbonamenti_per_id.values())

    def get_lista_contratti(self):
        return list(self._contratti_per_id.values())

    def get_abbonamento_per_id(self, id_abbonamento: int):
        return self._abbonamenti_per_id.get(id_abbonamento)

    def get_contratto_per_id(self, id_contratto: int):
        return self._contratti_per_id.get(id_contratto)

    def get_contratto_atleta(self, id_atleta: int) -> Optional[ContrattoAbbonamento]:
        for contratto in self._contratti_per_id.values():
            if id_atleta == contratto.get_id_atleta():
                return contratto
        return None

    def controllo_scadenze(self, giorni_anticipo: int = 1):
        data_target = datetime.date.today() + datetime.timedelta(days=giorni_anticipo)
        return [
            contratto for contratto in self._contratti_per_id.values() if contratto.get_scadenza() == data_target
        ]

    def controllo_tipo_abbonamento(self, id_contratto: int, tipo: str):
        contratto_abbonamento = self._contratti_per_id.get(id_contratto)

        if contratto_abbonamento is not None and contratto_abbonamento.get_tipologia() == tipo:
            return True
        return False

    def controllo_abbonamento_scaduto(self, id_contratto: int):
        contratto_abbonamento = self._contratti_per_id.get(id_contratto)

        if contratto_abbonamento is None:
            return True
        return datetime.date.today() >= contratto_abbonamento.get_scadenza()

    def carica_abbonamenti(self, lista_abbonamenti: list[Abbonamento]):
        self._abbonamenti_per_id = {
            abbonamento.get_id(): abbonamento for abbonamento in lista_abbonamenti
        }

    def carica_contratti(self, lista_contratti: list[ContrattoAbbonamento]):
        self._contratti_per_id = {
            contratto.get_id(): contratto for contratto in lista_contratti
        }

    def crea_contratto(self, id_atleta: int, id_abbonamento: int, data_inizio_opzionale: Optional[datetime.date] = None) -> Optional[ContrattoAbbonamento]:
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)
        abbonamento = self._abbonamenti_per_id.get(id_abbonamento)

        if abbonamento is None or atleta is None:
            return None

        for contratto in self._contratti_per_id.values():
            if contratto.get_id_atleta() == id_atleta and contratto.get_id_abbonamento() == id_abbonamento:
                return None

        abbonamento = self._abbonamenti_per_id.get(id_abbonamento)
        data_inizio = data_inizio_opzionale if data_inizio_opzionale is not None else datetime.date.today()
        nuovo_contratto = ContrattoAbbonamento(id_atleta, id_abbonamento, abbonamento.get_durata(), abbonamento.get_tipo(), data_inizio)

        self._contratti_per_id.update({nuovo_contratto.get_id(): nuovo_contratto})
        atleta.assegna_abbonamento(nuovo_contratto.get_id())
        return nuovo_contratto

    def crea_abbonamento(self, durata: int, tipo: str) -> Optional[Abbonamento]:
        nome_nuovo_abbonamento = f"{durata}-{tipo}"

        for abbonamento in self._abbonamenti_per_id.values():
            if abbonamento.get_nome() == nome_nuovo_abbonamento:
                return None

        nuovo_abbonamento = Abbonamento(durata, tipo)
        self._abbonamenti_per_id.update({nuovo_abbonamento.get_id(): nuovo_abbonamento})

        return nuovo_abbonamento