from domain.entities.utente import Utente

class Atleta (Utente):
    def __init__(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str= None, civico: int= None,
                 citta: str= None, provincia: str= None, cap: int= None):
        super().__init__(nome, cognome, sesso, nascita, codice_fiscale, via, civico, citta,
                         provincia, cap)

    def getRuolo(self):
        return "atleta"