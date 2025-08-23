import datetime

from domain.attività.allenatore import Allenatore
from domain.servizio.corso import Corso

from domain.attività.atleta import Atleta

from domain.attività.contratto_atleta_corso import ContrattoAtletaCorso

class GestoreCorsi:

    def __init__(self):
        self._lista_corsi = []
        self._lista_contratti_atleti= []
        self._lista_contratti_allenatori= []

    def get_lista_corsi(self):
        return self._lista_corsi

    def get_lista_contratti_atleti(self):
        return self._lista_contratti_atleti

    def get_lista_contratti_allenatori(self):
        return self._lista_contratti_allenatori

    def get_corso(self, nome_corso: str):
        for corso in self._lista_corsi:
            if corso.get_nome() == nome_corso:
                return corso
        return None

    def get_corsi_in_partenza(self):
        risultato = []

        for corso in self._lista_corsi:
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

    def get_contratto_allenatore_corso(self, corso: Corso):
        for contratto in self._lista_contratti_allenatori:
            if contratto.get_corso() == corso:
                return True

    def get_contratto_atleta_corso(self, corso: Corso, atleta: Atleta):
        for contratto in self._lista_contratti_allenatori:
            if contratto.get_corso() == corso and contratto.get_atleta() == atleta:
                return contratto
        return None

    def set_lista_corsi(self, lista_corsi):
        self._lista_corsi = lista_corsi

    def set_lista_contratti_atleti(self, lista_contratti):
        self._lista_contratti_atleti = lista_contratti

        for contratto in self._lista_contratti_atleti:
            corso = contratto.get_corso()
            corso.aggiungi_iscritto(contratto)

            atleta = contratto.get_atleta()
            atleta.aggiungi_iscritto(contratto)

    def set_lista_contratti_allenatori(self, lista_contratti_allenatori):
        self._lista_contratti_allenatori = lista_contratti_allenatori

        for contratto in self._lista_contratti_allenatori:
            corso = contratto.get_corso()
            corso.assegna_allenatore(contratto)

            allenatore = contratto.get_allenatore()
            allenatore.aggiungi_corso(contratto)

    def set_stato_corso(self, nome_corso: str, stato: bool):
        corso = self.get_corso(nome_corso)
        if corso is None:
            return False
        elif corso.get_stato == stato:
            return True
        else:
            corso.set_status(stato)
            return True

    def aggiungi_corso(self, nome: str, orario_corso: str):
        da_aggiungere = Corso(nome, orario_corso)
        self._lista_corsi.append(da_aggiungere)

    def iscrivi_atleta(self, atleta: Atleta, nome_corso: str):
        corso = self.get_corso(nome_corso)
        if corso is None:
            return False
        else:
            lista_iscrizioni = corso.get_lista_iscrizioni()
            for iscrizione in lista_iscrizioni:
                if iscrizione.get_atleta() == atleta:
                    return True
                else:
                    iscrizione = ContrattoAtletaCorso(atleta, corso, datetime.date.today().__str__())
                    self._lista_contratti_atleti.append(iscrizione)
                    corso.aggiungi_iscritto(iscrizione)
                    atleta.aggiungi_iscrizione(iscrizione)
                    return True