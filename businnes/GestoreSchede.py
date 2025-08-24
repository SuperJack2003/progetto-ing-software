import datetime

from domain.attività.allenatore import Allenatore
from domain.attività.atleta import Atleta
from domain.servizio.scheda import Scheda
from domain.servizio.esercizio import Esercizio

from domain.attività.contratto_esercizio import ContrattoEsercizio
from domain.attività.contratto_scheda import ContrattoScheda

class GestoreSchede:

    def __init__(self):
        self._lista_schede = []
        self._lista_esercizi = []
        self._lista_contratti_esercizi = {}
        self._lista_contratti_schede = {}

    def get_lista_schede(self):
        return self._lista_schede

    def get_lista_esercizi(self):
        return self._lista_esercizi

    def get_lista_contratti_esercizi(self):
        return self._lista_contratti_esercizi

    def get_lista_contratti_schede(self):
        return self._lista_contratti_schede

    def get_scheda(self, id_scheda: int):
        for scheda in self._lista_schede:
            if scheda.get_id() == id_scheda:
                return scheda

    def get_esercizio(self, nome: str):
        for esercizio in self._lista_esercizi:
            if esercizio.get_nome() == nome:
                return esercizio

    def get_contratto_esercizio(self, id_scheda: int, nome_esercizio: str):
        scheda = self.get_scheda(id_scheda)
        esercizio = self.get_esercizio(nome_esercizio)

        if scheda and esercizio:
            if scheda in self._lista_contratti_esercizi.keys():
                for contratto in self._lista_contratti_esercizi.get(scheda):
                    if contratto.get_esercizio == esercizio:
                        return contratto

        return None

    def get_esercizi_scheda(self, id_scheda: int):
        return self._lista_contratti_esercizi[self.get_scheda(id_scheda)]

    def get_schede_atleta(self, id_atleta: int):
        return self._lista_contratti_schede[id_atleta]

    def get_scheda_attiva(self, id_atleta: int):
        lista_contratti = self._lista_contratti_schede[id_atleta]

        for contratto in lista_contratti:
            if contratto.get_stato():
                return contratto

        return None

    def set_lista_schede(self, lista_schede: list[Scheda]):
        self._lista_schede = lista_schede

    def set_lista_esercizi(self, lista_esercizi: list[Esercizio]):
        self._lista_esercizi = lista_esercizi

    def set_lista_contratti_esercizi(self, lista_contratti: list[ContrattoEsercizio]):
        for contratto in lista_contratti:
            key = contratto.get_scheda()
            if key in self._lista_contratti_esercizi.keys():
                if not contratto in self._lista_contratti_esercizi[key]:
                    self._lista_contratti_esercizi[key].append(contratto)
            else:
                self._lista_contratti_esercizi.update({key: [contratto]})

    def set_lista_contratti_schede(self, lista_contratti: list[ContrattoScheda]):
        for contratto in lista_contratti:
            key = contratto.get_atleta()
            if key in self._lista_contratti_schede.keys():
                if not contratto in self._lista_contratti_schede[key]:
                    self._lista_contratti_schede[key].append(contratto)
            else:
                self._lista_contratti_schede.update({key: [contratto]})

    def togli_contratto_esercizio(self, id_scheda: int, nome_esercizio: str):
        contrato_esercizio = self.get_contratto_esercizio(id_scheda, nome_esercizio)

        if contrato_esercizio:
            scheda = self.get_scheda(id_scheda)

            if scheda in self._lista_contratti_esercizi.keys():
                if contrato_esercizio in self._lista_contratti_esercizi.get(scheda):
                    self._lista_contratti_esercizi[scheda].remove(contrato_esercizio)
                    return True

        return False

    def disattiva_scheda(self, atleta: Atleta):
        if atleta in self._lista_contratti_esercizi.keys():
            for contratto in self._lista_contratti_esercizi[atleta]:
                if contratto.get_stato():
                    contratto.set_stato(False)
                    return True

        return False

    def aggiungi_scheda(self, id_allenatore: int):
        nuova_scheda = Scheda(id_allenatore, datetime.date.today().__str__())
        self._lista_schede.append(nuova_scheda)

    def aggiungi_esercizio(self, nome_esercizio: str, descrizione: str, percorso_gif: str= None):
        if not self.get_esercizio(nome_esercizio):
            nuovo_esercizio = Esercizio(nome_esercizio, descrizione, percorso_gif)
            self._lista_esercizi.append(nuovo_esercizio)

    def aggiungi_contratto_esercizio(self, id_scheda: int, nome_esercizio: str, serie: int, ripetizioni: int,
                                     recupero: int, modalità: str = None):
        scheda = self.get_scheda(id_scheda)
        esercizio = self.get_esercizio(nome_esercizio)

        if scheda and esercizio:

            # Controllo che non esista già l'esercizio nella scheda
            if scheda in self._lista_contratti_esercizi.keys():
                for contratto in self._lista_contratti_esercizi[scheda]:
                    if esercizio in contratto.get_esercizio():
                        return False

            nuovo_contratto = ContrattoEsercizio(esercizio, scheda, datetime.date.today().__str__(), serie, ripetizioni,
                                                 recupero, modalità)

            if scheda in self._lista_contratti_esercizi.keys():
                self._lista_contratti_esercizi[scheda].append(nuovo_contratto)
            else:
                self._lista_contratti_esercizi.update({scheda: [nuovo_contratto]})

            scheda.aggiungi_esercizio(nuovo_contratto)
            return True

    def aggiungi_contratto_scheda(self, atleta: Atleta, id_scheda: int, creatore: Allenatore, durata: int):
        scheda = self.get_scheda(id_scheda)

        if scheda:

            #Controllo se il contratto esiste già
            if atleta in self._lista_contratti_schede.keys():
                if scheda in self._lista_contratti_schede[atleta]:
                   return False

            nuovo_contratto = ContrattoScheda(atleta, scheda, creatore, durata,  datetime.date.today().__str__())
            self.disattiva_scheda(atleta)

            if atleta in self._lista_contratti_esercizi.keys():
                self._lista_contratti_esercizi[atleta].append(nuovo_contratto)
            else:
                 self._lista_contratti_schede.update({atleta: [nuovo_contratto]})

            atleta.assegna_scheda(nuovo_contratto)
            return True