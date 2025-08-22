from domain.attività.contratto_atleta_allenatore import ContrattoAtletaAllenatore
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

    def get_ruolo(self):
        return "allenatore"

    def get_lista_corsi(self):
        return self._lista_corsi

    def get_lista_atleti(self):
        return self._lista_atleti

    def aggiungi_corso(self, corso):
        self._lista_corsi.append(corso)

    def aggiungi_atleta(self, contratto_atleta: ContrattoAtletaAllenatore):
        self._lista_atleti.append(contratto_atleta)