from domain.attività.allenatore import Allenatore

class GestoreAllenatore:

    def __init__(self):
        self._lista_allenatori = []

    def get_lista_allenatori(self):
        return self._lista_allenatori

    def get_allenatore_per_id(self, da_cercare: int):
        for allenatore in self._lista_allenatori:
            if allenatore.get_id() == da_cercare:
                return allenatore
        return None

    def get_allenatore_per_nome(self, da_cercare: str):
        omonimi = []

        for allenatore in self._lista_allenatori:
            if allenatore.__str__() == da_cercare:
                omonimi.append(allenatore)

        if not omonimi:
            return None

        return omonimi

    def controllo_email(self, email):
        for allenatore in self._lista_allenatori:
            if allenatore.get_email() == email:
                return True
        return False

    def controllo_tel(self, tel):
        for allenatore in self._lista_allenatori:
            if allenatore.get_tel() == tel:
                return True
        return False

    def set_lista_allenatori(self, lista):
        self._lista_allenatori = lista

    def aggiungi_allenatore(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str = None, civico: int= None,
                 citta: str = None, provincia: str = None, cap: int = None,
                 telefono: str = None, email: str = None):

        if not self.controllo_email(email) and not self.controllo_tel(telefono):
            allenatore = Allenatore(nome, cognome, sesso, nascita, codice_fiscale, via, civico,citta, provincia, cap, telefono, email)
            self._lista_allenatori.append(allenatore)