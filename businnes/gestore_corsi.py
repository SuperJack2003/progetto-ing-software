import datetime

from domain.servizio.corso import Corso

from domain.attività.contratto_allenatore_corso import ContrattoAllenatoreCorso
from domain.attività.contratto_atleta_corso import ContrattoAtletaCorso

from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori

class GestoreCorsi:

    def __init__(self):
        self._lista_corsi = {}
        self._lista_contratti_atleti = {}
        self._lista_contratti_allenatori = {}

        self._gestore_atleti = None
        self._gestore_allenatori = None

    def get_lista_corsi(self):
        lista_corsi = []

        for id_corso in self._lista_corsi.keys():
            lista_corsi.append(self._lista_corsi[id_corso])

        return lista_corsi

    def get_lista_contratti_atleti(self):
        lista_contratti = []

        for id_contratto in self._lista_contratti_atleti.keys():
            lista_contratti.append(self._lista_contratti_atleti[id_contratto])

        return lista_contratti

    def get_lista_contratti_allenatori(self):
        lista_contratti = []

        for id_contratto in self._lista_contratti_allenatori.keys():
            lista_contratti.append(self._lista_contratti_allenatori[id_contratto])

        return lista_contratti

    def get_corso(self, id_corso: int):
        return self._lista_corsi[id_corso]

    def get_corsi_in_partenza(self):
        risultato = []

        for id_corso in self._lista_corsi.keys():
            corso = self._lista_corsi[id_corso]

            orari_corso = corso.get_orari_corso()
            orari_corso = orari_corso.split(",") #Divisione della stringa per prendere i giorni

            for data in orari_corso:
                giorno = data.split(" ")[0] #Giorno (a lettere)

                traduzione_giorni = {"Monday": "Lunedì",
                                     "Tuesday": "Martedì",
                                     "Wednesday": "Mercoledì",
                                     "Thursday": "Giovedì",
                                     "Friday": "Venerdì",
                                     "Saturday": "Sabato",
                                     "Sunday": "Domenica"}

                domani = traduzione_giorni.get((datetime.date.today() + datetime.timedelta(days=1)).strftime("%A")) #Giorno di domani, preso e tradotto in italiano

                if giorno == domani:
                    risultato.append(corso)

        return risultato

    def get_contratto_allenatore_corso(self, id_contratto: int):
        return self._lista_contratti_allenatori[id_contratto]

    def get_contratto_da_allenatore(self, id_allenatore: int):
        for id_contratto in self._lista_contratti_allenatori.keys():
            contratto = self._lista_contratti_allenatori[id_contratto]
            if contratto.get_allenatore() == id_allenatore:
                return contratto
        return None

    def get_contratto_atleta_corso(self, id_contratto: int):
        return self._lista_contratti_atleti[id_contratto]

    def get_contratti_da_atleta(self, id_atleta: int):
        risultato = []

        for id_contratto in self._lista_contratti_allenatori.keys():
            contratto = self._lista_contratti_allenatori[id_contratto]
            if contratto.get_atleta() == id_atleta:
                risultato.append(contratto)

        if risultato:
            return risultato
        return None

    def set_gestori(self, gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori):
        self._gestore_atleti = gestore_atleti
        self._gestore_allenatori = gestore_allenatori

    def set_lista_corsi(self, lista_corsi: list[Corso]):
        for corso in lista_corsi:
            if corso.get_id not in self._lista_corsi.keys():
                self._lista_corsi.update({corso.get_id: corso})

    def set_lista_contratti_atleti(self, lista_contratti: list[ContrattoAtletaCorso]):
        for contratto in lista_contratti:
            if contratto.get_id not in self._lista_contratti_atleti.keys():
                self._lista_contratti_atleti.update({contratto.get_id: contratto})
                self._gestore_atleti.get_atleta_per_id(contratto.get_atleta).aggiungi_iscrizione(contratto.get_id)

    def set_lista_contratti_allenatori(self, lista_contratti_allenatori: list[ContrattoAllenatoreCorso]):
        for contratto in lista_contratti_allenatori:
            if contratto.get_id not in self._lista_contratti_allenatori.keys():
                self._lista_contratti_allenatori.update({contratto.get_id: contratto})
                self._gestore_allenatori.get_allenatore_per_id(contratto.get_allenatore).aggiungi_corso(contratto.get_id)

    def set_stato_corso(self, id_corso: int, stato: bool):
        corso = self._lista_corsi[id_corso]

        if corso is None:
            return False

        corso.set_stato(stato)

        return True

    def aggiungi_corso(self, nome: str, orario_corso: str):
        for id_corso in self._lista_corsi.keys():
            corso = self._lista_corsi[id_corso]
            if corso.get_nome() == nome:
                return False

        nuovo_corso = Corso(nome, orario_corso)
        self._lista_corsi.update({nuovo_corso.get_id: nuovo_corso})

        return True

    def iscrivi_atleta(self, id_atleta: int, id_corso: int):
        corso = self._lista_corsi[id_corso]
        atleta = self._gestore_atleti.get_atleta_per_id(id_atleta)

        if corso is None or atleta is None:
            return False

        nuovo_contratto = ContrattoAtletaCorso(id_atleta, id_corso, datetime.date.today())
        self._lista_contratti_atleti.update({nuovo_contratto.get_id: nuovo_contratto})
        atleta.aggiungi_iscrizione(nuovo_contratto.get_id)

        return True

    def assegna_allenatore(self, id_allenatore: int, id_corso: int):
        corso = self._lista_corsi[id_corso]
        allenatore = self._gestore_allenatori.get_allenatore_per_id(id_allenatore)

        if corso is None or allenatore is None:
            return False

        nuovo_contratto = ContrattoAllenatoreCorso(id_allenatore, id_corso, datetime.date.today())
        self._lista_contratti_allenatori.update({nuovo_contratto.get_id: nuovo_contratto})
        allenatore.aggiungi_corso(nuovo_contratto.get_id)

        return True