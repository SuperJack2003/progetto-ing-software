from domain.attività.utente import Utente

from domain.attività.contratto_atleta_corso import ContrattoAtletaCorso

class Atleta (Utente):
    def __init__(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str= None, civico: int= None,
                 citta: str= None, provincia: str= None, cap: int= None,
                 telefono: str= None, email: str= None):
        super().__init__(nome, cognome, sesso, nascita, codice_fiscale, via, civico, citta,
                         provincia, cap, telefono, email)
        self._contratto_atleta_allenatore = None
        self._contratto_abbonamento = None
        self._iscrizioni_corsi = []

    def get_ruolo(self):
        return "atleta"

    def get_contratto_atleta_allenatore(self):
        return self._contratto_atleta_allenatore

    def get_contratto_abbonamento(self):
        return self._contratto_abbonamento

    def aggiungi_iscrizione(self, iscrizione: ContrattoAtletaCorso):
        self._iscrizioni_corsi.append(iscrizione)