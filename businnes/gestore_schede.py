import datetime

from domain.attività.allenatore import Allenatore
from domain.attività.atleta import Atleta
from domain.servizio.scheda import Scheda
from domain.servizio.esercizio import Esercizio

from domain.attività.contratto_esercizio import ContrattoEsercizio
from domain.attività.contratto_scheda import ContrattoScheda

from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori
from businnes.gestore_abbonamenti import GestoreAbbonamenti

class GestoreSchede:

    def __init__(self):
        self._lista_schede = {}
        self._lista_esercizi = {}
        self._lista_contratti_esercizi = {}
        self._lista_contratti_schede = {}

        self._gestore_atleti = None
        self._gestore_allenatori = None
        self._gestore_abbonamenti = None

    def get_lista_schede(self):
        lista_schede = []

        for id_scheda in self._lista_schede.keys():
            lista_schede.append(self._lista_schede[id_scheda])

        return lista_schede

    def get_lista_esercizi(self):
        lista_esercizi = []

        for id_esercizio in self._lista_esercizi.keys():
            lista_esercizi.append(self._lista_esercizi[id_esercizio])

        return lista_esercizi

    def get_lista_contratti_esercizi(self):
        lista_contratti = []

        for scheda in self._lista_contratti_esercizi.keys():
            lista_contratti.append(self._lista_contratti_esercizi[scheda])

        return lista_contratti

    def get_lista_contratti_schede(self):
        lista_contratti = []

        for atleta in self._lista_contratti_schede.keys():
            lista_contratti.append(self._lista_contratti_schede[atleta])

        return lista_contratti

    def get_scheda(self, id_scheda: int):
        return self._lista_schede[id_scheda]

    def get_schede_atleta(self, id_atleta: int):
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)

        if atleta is not None:
            return self._lista_contratti_schede[atleta]
        return None

    def get_scheda_attiva(self, id_atleta: int):
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)
        lista_contratti = self._lista_contratti_schede[atleta]

        for contratto in lista_contratti:
            if contratto.get_stato():
                return contratto

        return None

    def get_esercizio(self, id_esercizio: int):
        return self._lista_esercizi[id_esercizio]

    def get_contratto_esercizio(self, id_scheda: int, id_esercizio: int):
        esercizio = self._lista_esercizi[id_esercizio]
        scheda = self._lista_schede[id_scheda]

        if esercizio is not None and scheda is not None:
            lista_contratti = self._lista_contratti_esercizi[scheda]
            for contratto in lista_contratti:
                if contratto.get_esercizio == id_esercizio:
                    return contratto

        return None

    def get_esercizi_scheda(self, id_scheda: int):
        scheda = self._lista_schede[id_scheda]
        return self._lista_contratti_esercizi[scheda]

    def set_gestori(self, gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori, gestore_abbonamenti: GestoreAbbonamenti):
        self._gestore_atleti = gestore_atleti
        self._gestore_allenatori = gestore_allenatori
        self._gestore_abbonamenti = gestore_abbonamenti

    def set_lista_schede(self, lista_schede: list[Scheda]):
        for scheda in lista_schede:
            if scheda.get_id() not in self._lista_schede.keys():
                self._lista_schede.update({scheda.get_id(): scheda})
                allenatore = self._lista_schede[scheda.get_id_allenatore()]
                if allenatore is not None:
                    allenatore.aggiungi_scheda(scheda.get_id())

    def set_lista_esercizi(self, lista_esercizi: list[Esercizio]):
        for esercizio in lista_esercizi:
            if esercizio.get_id() not in self._lista_esercizi.keys():
                self._lista_esercizi.update({esercizio.get_id(): esercizio})

    def set_lista_contratti_esercizi(self, lista_contratti: list[ContrattoEsercizio]):
        for contratto in lista_contratti:
            scheda = self._lista_schede[contratto.get_scheda()]
            if scheda in self._lista_contratti_esercizi.keys():
                self._lista_contratti_esercizi[scheda].append(contratto)
            else:
                self._lista_contratti_esercizi.update({scheda: [contratto]})

    def set_lista_contratti_schede(self, lista_contratti: list[ContrattoScheda]):
        for contratto in lista_contratti:
            atleta = self._gestore_atleti.get_atleta_per_id(contratto.get_atleta())
            if atleta in self._lista_contratti_schede.keys():
                self._lista_contratti_schede[atleta].append(contratto)
            else:
                self._lista_contratti_schede.update({atleta: [contratto]})

    def togli_contratto_esercizio(self, id_scheda: int, id_esercizio: int):
        scheda = self._lista_schede[id_scheda]
        lista_contratti = self._lista_contratti_esercizi[scheda]

        for contratto in lista_contratti:
            if contratto.get_esercizio() == id_esercizio:
                self._lista_contratti_esercizi[scheda].remove(contratto)

    def disattiva_scheda(self, id_atleta: int):
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)

        if atleta in self._lista_contratti_schede.keys():
            self.get_scheda_attiva(id_atleta).set_stato(False)

    def aggiungi_scheda(self, id_allenatore: int):
        allenatore = self._gestore_allenatori.get_allenatore_per_id(id_allenatore)

        if allenatore is None:
            return False

        nuova_scheda = Scheda(id_allenatore, datetime.date.today())
        self._lista_schede.update({nuova_scheda.get_id(): nuova_scheda})
        allenatore.aggiungi_scheda(nuova_scheda.get_id())

        return True

    def aggiungi_esercizio(self, nome_esercizio: str, descrizione: str, percorso_gif: str= None):
        for id_esercizio in self._lista_esercizi.keys():
            esercizio = self._lista_esercizi[id_esercizio]
            if esercizio.get_nome() == nome_esercizio:
                return False

        nuovo_esercizio = Esercizio(nome_esercizio, descrizione, percorso_gif)
        self._lista_esercizi.update({nuovo_esercizio.get_id(): nuovo_esercizio})

        return True

    def aggiungi_contratto_esercizio(self, id_scheda: int, id_esercizio: int, serie: int, ripetizioni: int,
                                     recupero: int, modalità: str = None):
        scheda = self._lista_schede[id_scheda]
        esercizio = self._lista_esercizi[id_esercizio]

        if scheda is None or esercizio is None:
            return False

        if scheda in self._lista_contratti_esercizi.keys():
            for es in self._lista_contratti_esercizi[scheda]:
                if es.get_id() == id_esercizio:
                    return False

        nuovo_contratto = ContrattoEsercizio(id_esercizio, id_scheda, datetime.date.today(), serie, ripetizioni, recupero, modalità)

        if scheda in self._lista_contratti_esercizi.keys():
            self._lista_contratti_esercizi[scheda].append(nuovo_contratto)
        else:
            self._lista_contratti_esercizi.update({scheda: [nuovo_contratto]})

        scheda.aggiungi_contratto(nuovo_contratto.get_id())

        return True

    def aggiungi_contratto_scheda(self, id_atleta, id_scheda: int, id_allenatore: int, durata: int):
        scheda = self._lista_schede[id_scheda]
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)
        allenatore = self._gestore_allenatori.get_allenatore_per_id(id_allenatore)

        if scheda is None or atleta is None or allenatore is None:
            return False

        if not self._gestore_abbonamenti.controllo_tipo_abbonamento(atleta.get_abbonamento(), "corsi+sala"):
            return False

        nuovo_contratto = ContrattoScheda(id_atleta, id_scheda, id_allenatore, durata, datetime.date.today())

        if atleta in self._lista_contratti_schede.keys():
            self._lista_contratti_schede[atleta].append(nuovo_contratto)
        else:
            self._lista_contratti_schede.update({atleta: [nuovo_contratto]})

        self.disattiva_scheda(id_atleta)
        atleta.assegna_scheda(nuovo_contratto.get_id())

        return True