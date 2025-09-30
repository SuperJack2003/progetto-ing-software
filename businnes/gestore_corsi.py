import datetime
from typing import Optional

from domain.servizio.corso import Corso

from domain.attività.contratto_allenatore_corso import ContrattoAllenatoreCorso
from domain.attività.contratto_atleta_corso import ContrattoAtletaCorso

from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori

_traduzione_corsi = {
    "Monday": "Lunedì",
    "Tuesday": "Martedì",
    "Wednesday": "Mercoledì",
    "Thursday": "Giovedì",
    "Friday": "Venerdì",
    "Saturday": "Sabato",
    "Sunday": "Domenica",
}

class GestoreCorsi:

    def __init__(self, gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori):
        self._corsi_per_id = {}
        self._contratti_atleti_per_id = {}
        self._contratti_allenatori_per_id = {}

        self._gestore_atleti = gestore_atleti
        self._gestore_allenatori = gestore_allenatori

    def get_lista_corsi(self):
        return list(self._corsi_per_id.values())

    def get_lista_contratti_atleti(self):
        return list(self._contratti_atleti_per_id.values())

    def get_lista_contratti_allenatori(self):
        return list(self._contratti_allenatori_per_id.values())

    def get_corso(self, id_corso: int):
        return self._corsi_per_id.get(id_corso)

    def get_iscritti_corso(self, id_corso: int) -> list[ContrattoAtletaCorso]:
        return [contratto for contratto in self._contratti_atleti_per_id.values() if contratto.get_id_corso() == id_corso]

    def get_allenatore_corso(self, id_corso: int) -> Optional[ContrattoAllenatoreCorso]:
        for contratto in self._contratti_allenatori_per_id.values():
            if contratto.get_id_corso() == id_corso:
                return contratto
        return None

    def get_corsi_in_partenza(self) -> list[Corso]:
        risultato = []

        for corso in self._corsi_per_id.values():
            programmazione_settimanale = corso.get_programmazione_settimanale()
            domani = _traduzione_corsi.get((datetime.date.today() + datetime.timedelta(days=1)).strftime("%A"))
            if programmazione_settimanale.controlla_giorno(domani):
                risultato.append(corso)

        return risultato

    def get_contratto_allenatore_corso(self, id_contratto: int):
        return self._contratti_allenatori_per_id.get(id_contratto)

    def get_contratti_allenatore(self, id_allenatore: int):
        return [contratto for contratto in self._contratti_allenatori_per_id.values() if contratto.get_id_allenatore() == id_allenatore]

    def get_contratto_atleta_corso(self, id_contratto: int):
        return self._contratti_atleti_per_id.get(id_contratto)

    def get_contratti_atleta(self, id_atleta: int):
        return [contratto for contratto in self._contratti_atleti_per_id.values() if contratto.get_id_atleta() == id_atleta]

    def carica_corsi(self, lista_corsi: list[Corso]):
        self._corsi_per_id = {corso.get_id(): corso for corso in lista_corsi}

    def carica_contratti_atleti(self, lista_contratti: list[ContrattoAtletaCorso]):
        self._contratti_atleti_per_id = {contratto.get_id(): contratto for contratto in lista_contratti}

    def carica_contratti_allenatori(self, lista_contratti_allenatori: list[ContrattoAllenatoreCorso]):
        self._contratti_allenatori_per_id = {contratto.get_id(): contratto for contratto in lista_contratti_allenatori}

    def set_stato_corso(self, id_corso: int, stato: bool) -> bool:
        corso = self._corsi_per_id.get(id_corso)

        if corso is None:
            return False

        corso.set_stato(stato)

        return True

    def aggiungi_corso(self, nome: str, descrizione: str, eta_min: int, eta_max: int, orari_corso: str) -> Optional[Corso]:
        for corso in self._corsi_per_id.values():
            if corso.get_nome() == nome:
                return None

        nuovo_corso = Corso(nome, descrizione, eta_min, eta_max, orari_corso)
        self._corsi_per_id.update({nuovo_corso.get_id(): nuovo_corso})

        return nuovo_corso

    def iscrivi_atleta(self, id_atleta: int, id_corso: int) -> Optional[ContrattoAtletaCorso]:
        corso = self._corsi_per_id.get(id_corso)
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)

        if corso is None or atleta is None:
            return None

        for contratto in self._contratti_atleti_per_id.values():
            if contratto.get_id_atleta() == id_atleta and contratto.get_id_corso() == id_corso:
                return None

        eta_min = corso.get_eta_min()
        eta_max = corso.get_eta_max()
        eta_atleta = atleta.get_eta()

        if eta_atleta < eta_min or eta_atleta > eta_max:
            return None

        nuovo_contratto = ContrattoAtletaCorso(id_atleta, id_corso, datetime.date.today())
        self._contratti_atleti_per_id.update({nuovo_contratto.get_id(): nuovo_contratto})
        atleta.aggiungi_iscrizione(nuovo_contratto.get_id())

        return nuovo_contratto

    def assegna_allenatore(self, id_allenatore: int, id_corso: int) -> Optional[ContrattoAllenatoreCorso]:
        corso = self._corsi_per_id.get(id_corso)
        allenatore = self._gestore_allenatori.get_allenatore_per_id(id_allenatore)

        if corso is None or allenatore is None:
            return None

        for contratto in self._contratti_allenatori_per_id.values():
            if contratto.get_id_corso() == id_corso:
                return None

        nuovo_contratto = ContrattoAllenatoreCorso(id_allenatore, id_corso, datetime.date.today())
        self._contratti_allenatori_per_id.update({nuovo_contratto.get_id(): nuovo_contratto})
        allenatore.aggiungi_corso(nuovo_contratto.get_id())

        return nuovo_contratto