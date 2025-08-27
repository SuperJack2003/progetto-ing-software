from domain.attività.atleta import Atleta

class GestoreAtleti:

    def __init__(self):
        self._lista_atleti = {}

    def get_lista_atleti(self):
        lista_atleti = []

        for id_atleta in self._lista_atleti.keys():
            lista_atleti.append(self._lista_atleti[id_atleta])

        return lista_atleti

    def get_atleta_per_id(self, id_da_cercare: int):
        return self._lista_atleti[id_da_cercare]

    def get_atleta_da_nome(self, nome_da_cercare: str):
        omonimi = []

        for id_atleta in self._lista_atleti.keys():
            if nome_da_cercare == self._lista_atleti[id_atleta].__str__():
                omonimi.append(self._lista_atleti[id_atleta])

        if omonimi:
            return omonimi
        return None

    def controllo_email(self, email: str):
        for id_atleta in self._lista_atleti.keys():
            if email == self._lista_atleti[id_atleta].get_email():
                return True
        return False

    def controllo_tel(self, tel: str):
        for id_atleta in self._lista_atleti.keys():
            if tel == self._lista_atleti[id_atleta].get_telefono():
                return True
        return False

    def set_lista_atleti(self, lista_atleti: list[Atleta]):
        for atleta in lista_atleti:
            if atleta.get_id() not in self._lista_atleti.keys():
                self._lista_atleti.update({atleta.get_id(): atleta})

    def aggiungi_atleta(self, nome: str, cognome: str, sesso: chr, nascita: str,
                 codice_fiscale: str = None, via: str= None, civico: int= None,
                 citta: str= None, provincia: str= None, cap: int= None,
                 telefono: str= None, email: str= None):

        if not self.controllo_email(email) and not self.controllo_tel(telefono):
            atleta = Atleta(nome, cognome, sesso, nascita, codice_fiscale, via, civico,citta, provincia, cap, telefono, email)
            self._lista_atleti.update({atleta.get_id(): atleta})
            return True

        return False