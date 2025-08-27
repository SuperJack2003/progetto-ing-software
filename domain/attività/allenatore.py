from domain.attività.utente import Utente

class Allenatore(Utente):
    def __init__(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str = None, civico: int= None,
                 citta: str = None, provincia: str = None, cap: int = None,
                 telefono: str = None, email: str = None):
        super().__init__(nome, cognome, sesso, nascita, codice_fiscale, via, civico, citta,
                         provincia, cap, telefono, email)
        self._lista_corsi = []
        self._lista_atleti = []
        self._lista_schede = []

    def get_ruolo(self):
        return "allenatore"

    def get_lista_corsi(self):
        return self._lista_corsi

    def get_lista_atleti(self):
        return self._lista_atleti

    def get_lista_schede(self):
        return self._lista_schede

    def aggiungi_corso(self, id_contratto_corso: int):
        self._lista_corsi.append(id_contratto_corso)

    def aggiungi_atleta(self, id_contratto_atleta: int):
        self._lista_atleti.append(id_contratto_atleta)

    def aggiungi_scheda(self, id_contratto_scheda: int):
        self._lista_schede.append(id_contratto_scheda)