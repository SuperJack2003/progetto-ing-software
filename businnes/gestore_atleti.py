from typing import Optional
from domain.attività.atleta import Atleta

class GestoreAtleti:

    def __init__(self):
        self._atleti_per_id = {}

    def get_lista_atleti(self):
        return list(self._atleti_per_id.values())

    def get_atleta_per_id(self, id_da_cercare: int):
        return self._atleti_per_id.get(id_da_cercare) if id_da_cercare in self._atleti_per_id.keys() else None

    def get_atleta_per_nome(self, nome_da_cercare: str):
        omonimi = [
            atleta for atleta in self._atleti_per_id.values() if nome_da_cercare == f"{atleta.get_nome()} {atleta.get_cognome()}"
        ]
        return omonimi

    def _controllo_email(self, email: str):
        for atleta in self._atleti_per_id.values():
            if email == atleta.get_email():
                return True
        return False

    def _controllo_tel(self, tel: str):
        for atleta in self._atleti_per_id.values():
            if tel == atleta.get_telefono():
                return True
        return False

    def carica_atleti(self, lista_atleti: list[Atleta]):
        self._atleti_per_id = {atleta.get_id(): atleta for atleta in lista_atleti}

    def aggiungi_atleta(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str= None, civico: int= None,
                 citta: str= None, provincia: str= None, cap: int= None,
                 telefono: str= None, email: str= None) -> Optional[Atleta]:

        if not self._controllo_email(email) and not self._controllo_tel(telefono):
            atleta = Atleta(nome, cognome, sesso, nascita, codice_fiscale, via, civico,citta, provincia, cap, telefono, email)
            self._atleti_per_id.update({atleta.get_id(): atleta})
            return atleta

        return None