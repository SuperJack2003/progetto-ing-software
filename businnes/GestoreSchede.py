

class GestoreSchede:

    def __init__(self):
        self._lista_schede = []
        self._lista_esercizi = []
        self._lista_contratti_esercizi = {}
        self._lista_contratti_atleti = {}

    def get_lista_schede(self):
        return self._lista_schede

    def get_lista_esercizi(self):
        return self._lista_esercizi

    def get_lista_contratti_esercizi(self):
        return self._lista_contratti_esercizi

    def get_lista_contratti_atleti(self):
        return self._lista_contratti_atleti

    def get_scheda(self, id_scheda: int):
        for scheda in self._lista_schede:
            if scheda.get_id() == id_scheda:
                return scheda

    def get_esercizio(self, nome: str):
        for esercizio in self._lista_esercizi:
            if esercizio.get_nome() == nome:
                return esercizio

    def get_esercizi_scheda(self, id_scheda: int):
        return self._lista_contratti_esercizi[self.get_scheda(id_scheda)]

    def get_schede_atleta(self, id_atleta: int):
        return self._lista_contratti_atleti[id_atleta]

    def get_scheda_attiva(self, id_atleta: int):
        lista_contratti = self._lista_contratti_atleti[id_atleta]

        for contratto in lista_contratti:
            if contratto.get_stato():
                return contratto

        return None