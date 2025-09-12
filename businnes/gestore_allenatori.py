import datetime
from typing import Optional

from domain.attività.allenatore import Allenatore

from domain.attività.contratto_atleta_allenatore import ContrattoAtletaAllenatore

from businnes.gestore_atleti import GestoreAtleti

class GestoreAllenatori:

    def __init__(self, gestore_atleti: GestoreAtleti):
        self._allenatori_per_id = {}
        self._contratti_per_id = {}

        self._gestore_atleti = gestore_atleti

    def get_lista_allenatori(self):
        return list(self._allenatori_per_id.values())

    def get_lista_contratti(self):
        return list(self._contratti_per_id.values())

    def get_allenatore_per_id(self, da_cercare: int):
        return self._allenatori_per_id.get(da_cercare) if da_cercare in self._allenatori_per_id.keys() else None

    def get_contratto_per_id(self, id_contratto: int):
        return self._contratti_per_id.get(id_contratto) if id_contratto in self._contratti_per_id.keys() else None

    def get_contratti_allenatore(self, id_allenatore: int):
        contratti_allenatore = [
            contratto for contratto in self._contratti_per_id.values() if contratto.get_id_allenatore() == id_allenatore
        ]
        return contratti_allenatore

    def get_allenatore_per_nome(self, da_cercare: str):
        omonimi = [
            allenatore for allenatore in self._allenatori_per_id.values() if da_cercare == f"{allenatore.get_nome()} {allenatore.get_cognome()}"
        ]
        return omonimi

    def _controllo_email(self, email: str):
        for allenatore in self._allenatori_per_id.values():
            if allenatore.get_email() == email:
                return True
        return False

    def _controllo_tel(self, tel: str):
        for allenatore in self._allenatori_per_id.values():
            if allenatore.get_telefono() == tel:
                return True
        return False

    def _controllo_esistenza_contratto(self, id_allenatore: int, id_atleta: int):
        for contratto in self._contratti_per_id.values():
            if contratto.get_id_allenatore() == id_allenatore and contratto.get_id_atleta() == id_atleta:
                return True
        return False

    def carica_allenatori(self, lista_allenatori: list[Allenatore]):
        self._allenatori_per_id = {allenatore.get_id(): allenatore for allenatore in lista_allenatori}


    def carica_contratti(self, lista_contratti: list[ContrattoAtletaAllenatore]):
        self._contratti_per_id = {contratto.get_id(): contratto for contratto in lista_contratti}

    def aggiungi_allenatore(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str = None, civico: int= None,
                 citta: str = None, provincia: str = None, cap: int = None,
                 telefono: str = None, email: str = None) -> Optional[Allenatore]:

        if self._controllo_email(email) or self._controllo_tel(telefono):
            return None

        allenatore = Allenatore(nome, cognome, sesso, nascita, codice_fiscale, via, civico, citta, provincia, cap, telefono, email)
        self._allenatori_per_id.update({allenatore.get_id(): allenatore})
        return allenatore

    def assegna_atleta_ad_allenatore(self, id_allenatore: int, id_atleta: int) -> Optional[ContrattoAtletaAllenatore]:
        allenatore = self._allenatori_per_id.get(id_allenatore)
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)

        if not allenatore or not atleta:
            return None

        if self._controllo_esistenza_contratto(id_allenatore, id_atleta):
            return None

        nuovo_contratto = ContrattoAtletaAllenatore(id_atleta, id_allenatore, datetime.date.today())
        self._contratti_per_id.update({nuovo_contratto.get_id(): nuovo_contratto})

        allenatore.aggiungi_atleta(nuovo_contratto.get_id())
        atleta.assegna_allenatore(nuovo_contratto.get_id())

        return nuovo_contratto