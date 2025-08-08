class Corso:
    def __init__(self, nome, orario_corso):
        self._nome = nome
        self._orario_corso = orario_corso
        self._stato = True
        self._lista_iscritti = []

