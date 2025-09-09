import datetime

from domain.attività.allenatore import Allenatore

from domain.attività.contratto_atleta_allenatore import ContrattoAtletaAllenatore

from businnes.gestore_atleti import GestoreAtleti

class GestoreAllenatori:

    def __init__(self):
        self._lista_allenatori = {}
        self._lista_contratti = {}

        self._gestore_atleti = None

    def get_lista_allenatori(self):
        lista_allenatori = []

        for id_allenatore in self._lista_allenatori.keys():
            lista_allenatori.append(self._lista_allenatori[id_allenatore])

        return lista_allenatori

    def get_lista_contratti(self):
        lista_contratti = []

        for allenatore in self._lista_contratti.keys():
            for contratto in self._lista_contratti[allenatore]:
                lista_contratti.append(contratto)

        return lista_contratti

    def get_allenatore_per_id(self, da_cercare: int):
        return self._lista_allenatori[da_cercare]

    def get_contratto_per_id(self, id_contratto: int):
        for allenatore in self._lista_contratti.keys():
            if id_contratto == self._lista_contratti[allenatore].get_id():
                return self._lista_contratti[allenatore]
        return None

    def get_contratti_allenatore(self, id_allenatore: int):
        allenatore = self.get_allenatore_per_id(id_allenatore)

        if allenatore is not None and allenatore in self._lista_contratti.keys():
            return self._lista_contratti[allenatore]
        return None

    def get_allenatore_per_nome(self, da_cercare: str):
        omonimi = []

        for id_allenatore in self._lista_allenatori.keys():
            if da_cercare == self._lista_allenatori[id_allenatore].__str__():
                omonimi.append(self._lista_allenatori[id_allenatore])

        if not omonimi:
            return None

        return omonimi

    def controllo_email(self, email: str):
        for id_allenatore in self._lista_allenatori.keys():
            if email == self._lista_allenatori[id_allenatore].get_email():
                return True
        return False

    def controllo_tel(self, tel: str):
        for id_allenatore in self._lista_allenatori.keys():
            if tel == self._lista_allenatori[id_allenatore].get_telefono():
                return True
        return False

    def set_gestori(self, gestore_atleti: GestoreAtleti):
        self._gestore_atleti = gestore_atleti

    def set_lista_allenatori(self, lista: list[Allenatore]):
        for allenatore in lista:
            if allenatore.get_id() not in self._lista_allenatori.keys():
                self._lista_allenatori.update({allenatore.get_id(): allenatore})


    def set_lista_contratti(self, lista_contratti: list[ContrattoAtletaAllenatore]):
        for contratto in lista_contratti:
            allenatore = self.get_allenatore_per_id(contratto.get_allenatore())

            if allenatore in self._lista_contratti.keys():
                self._lista_contratti[allenatore].append(contratto)
            else:
                self._lista_contratti.update({allenatore: [contratto]})

    def aggiungi_allenatore(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str = None, civico: int= None,
                 citta: str = None, provincia: str = None, cap: int = None,
                 telefono: str = None, email: str = None):

        if self.controllo_email(email) and self.controllo_tel(telefono):
            return False

        allenatore = Allenatore(nome, cognome, sesso, nascita, codice_fiscale, via, civico, citta, provincia, cap, telefono, email)
        self._lista_allenatori.update({allenatore.get_id(): allenatore})
        return True

    def aggiungi_contratto(self, id_allenatore: int, id_atleta: int):
        allenatore = self._lista_allenatori[id_allenatore]
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)

        if atleta is None or allenatore is None:
            return False

        for allenatore in self._lista_contratti.keys():
            contratto = self._lista_contratti[allenatore]
            if allenatore.get_id() == id_allenatore and contratto.get_atleta() == id_atleta:
                return False

        nuovo_contratto = ContrattoAtletaAllenatore(id_atleta, id_allenatore, datetime.date.today())

        if allenatore in self._lista_contratti.keys():
            self._lista_contratti[allenatore].append(nuovo_contratto)
        else:
            self._lista_contratti.update({allenatore: [nuovo_contratto]})

        allenatore.aggiungi_atleta(nuovo_contratto.get_id())
        atleta.assegna_allenatore(nuovo_contratto.get_id())

        return True