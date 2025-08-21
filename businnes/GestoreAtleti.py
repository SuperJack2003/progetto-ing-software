from domain.attività.atleta import Atleta

class GestoreAtleti:

    def __init__(self):
        self._lista_atleti = []

    def get_lista_atleti(self):
        return self._lista_atleti

    def get_atleta_da_id(self, id_da_cercare):
        for atleta in self._lista_atleti:
            if atleta.id == id_da_cercare:
                return atleta
        return None

    def get_atleta_da_nome(self, nome_da_cercare):
        omonimi = []
        for atleta in self._lista_atleti:
            if atleta.__str__() == nome_da_cercare:
                omonimi.append(atleta)

        if not omonimi:
            return None

        return omonimi[0]

    def controllo_email(self, email):
        for atleta in self._lista_atleti:
            if atleta.email == email:
                return True
        return False

    def controllo_tel(self, tel):
        for atleta in self._lista_atleti:
            if atleta.tel == tel:
                return True
        return False

    def set_lista_atleti(self, lista_atleti):
        self._lista_atleti = lista_atleti

    def aggiungi_atleta(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str= None, civico: int= None,
                 citta: str= None, provincia: str= None, cap: int= None,
                 telefono: str= None, email: str= None):

        if not self.controllo_email(email) and not self.controllo_tel(telefono):
            atleta = Atleta(nome, cognome, sesso, nascita, codice_fiscale, via, civico,citta, provincia, cap, telefono, email)
            self._lista_atleti.append(atleta)
            return True

        return False