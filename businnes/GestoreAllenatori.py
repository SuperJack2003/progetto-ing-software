import datetime

from domain.attività.allenatore import Allenatore
from domain.attività.atleta import Atleta

from domain.attività.contratto_atleta_allenatore import ContrattoAtletaAllenatore


class GestoreAllenatori:

    def __init__(self):
        self._lista_allenatori = []
        self._lista_contratti = {}

    def get_lista_allenatori(self):
        return self._lista_allenatori

    def get_lista_contratti(self):
        return self._lista_contratti

    def get_allenatore_per_id(self, da_cercare: int):
        for allenatore in self._lista_allenatori:
            if allenatore.get_id() == da_cercare:
                return allenatore
        return None

    def get_contratti_allenatore(self, id_allenatore: int):
        allenatore = self.get_allenatore_per_id(id_allenatore)

        if allenatore is not None and allenatore in self._lista_contratti.keys():
            return self._lista_contratti[allenatore]
        return None

    def get_allenatore_per_nome(self, da_cercare: str):
        omonimi = []

        for allenatore in self._lista_allenatori:
            if allenatore.__str__() == da_cercare:
                omonimi.append(allenatore)

        if not omonimi:
            return None

        return omonimi

    def controllo_email(self, email):
        for allenatore in self._lista_allenatori:
            if allenatore.get_email() == email:
                return True
        return False

    def controllo_tel(self, tel):
        for allenatore in self._lista_allenatori:
            if allenatore.get_tel() == tel:
                return True
        return False

    def set_lista_allenatori(self, lista):
        self._lista_allenatori = lista

    def set_lista_contratti(self, lista_contratti: list[ContrattoAtletaAllenatore]):
        for contratto in lista_contratti:
            allenatore = contratto.get_allenatore()

            if allenatore in self._lista_contratti.keys():
                self._lista_contratti[allenatore].append(contratto)
            else:
                self._lista_contratti.update({allenatore: [contratto]})

    def aggiungi_allenatore(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str = None, civico: int= None,
                 citta: str = None, provincia: str = None, cap: int = None,
                 telefono: str = None, email: str = None):

        if not self.controllo_email(email) and not self.controllo_tel(telefono):
            allenatore = Allenatore(nome, cognome, sesso, nascita, codice_fiscale, via, civico,citta, provincia, cap, telefono, email)
            self._lista_allenatori.append(allenatore)

    def aggiungi_contratto(self, atleta: Atleta, allenatore: Allenatore):
        nuovo_contratto = ContrattoAtletaAllenatore(atleta, allenatore, datetime.date.today().__str__())

        if allenatore in self._lista_contratti.keys():
            self._lista_contratti[allenatore].append(nuovo_contratto)
        else:
            self._lista_contratti.update({allenatore: [nuovo_contratto]})

        allenatore.aggiungi_atleta(nuovo_contratto)
        atleta.assegna_allenatore(nuovo_contratto)