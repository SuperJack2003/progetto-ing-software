class Corso:
    def __init__(self, nome: str, orario_corso: str):
        self._nome = nome
        self._orario_corso = orario_corso
        self._stato = True
        self._lista_iscritti = []

    def get_nome(self):
        return self._nome
