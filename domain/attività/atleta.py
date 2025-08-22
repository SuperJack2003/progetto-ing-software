from domain.attività.utente import Utente

from domain.attività.contratto_atleta_corso import ContrattoAtletaCorso

class Atleta (Utente):
    def __init__(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str= None, civico: int= None,
                 citta: str= None, provincia: str= None, cap: int= None,
                 telefono: str= None, email: str= None):
        super().__init__(nome, cognome, sesso, nascita, codice_fiscale, via, civico, citta,
                         provincia, cap, telefono, email)
        self._iscrizioni_corsi = []

    def get_ruolo(self):
        return "atleta"

    def aggiungi_iscrizione(self, iscrizione: ContrattoAtletaCorso):
        self._iscrizioni_corsi.append(iscrizione)