from domain.attività.utente import Utente

class Atleta (Utente):
    def __init__(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str= None, civico: int= None,
                 citta: str= None, provincia: str= None, cap: int= None,
                 telefono: str= None, email: str= None):

        super().__init__(nome, cognome, sesso, nascita, codice_fiscale, via, civico, citta,
                         provincia, cap, telefono, email)

        self._contratto_atleta_allenatore = None
        self._contratto_abbonamento = None
        self._contratto_scheda = []
        self._iscrizioni_corsi = []

    def get_ruolo(self):
        return "atleta"

    def get_contratto_atleta_allenatore(self):
        return self._contratto_atleta_allenatore

    def get_contratto_abbonamento(self):
        return self._contratto_abbonamento

    def aggiungi_iscrizione(self, id_iscrizione: int):
        self._iscrizioni_corsi.append(id_iscrizione)

    def assegna_abbonamento(self, id_contratto_abbonamento: int):
        self._contratto_abbonamento = id_contratto_abbonamento

    def assegna_scheda(self, id_contratto_scheda: int):
        self._contratto_scheda.append(id_contratto_scheda)

    def assegna_allenatore(self, id_contratto_allenatore: int):
        self._contratto_atleta_allenatore = id_contratto_allenatore