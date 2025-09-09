import datetime

from domain.servizio.notifica import Notifica

from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori

class GestoreNotifiche:

    def __init__(self):
        self._lista_notifiche = {}

        self._gestore_atleti = None
        self._gestore_allenatori = None

    def get_lista_notifiche(self):
        lista_notifiche = []

        for destinatario in self._lista_notifiche.keys():
            for notifica in self._lista_notifiche[destinatario]:
                lista_notifiche.append(notifica)

        return lista_notifiche

    def get_notifiche_da_utente(self, id_destinatario: int):
        destinatario = self._gestore_atleti.get_atleta_per_id(id_destinatario)
        if destinatario is None:
            destinatario = self._gestore_allenatori.get_allenatore_per_id(id_destinatario)
        if destinatario is None:
            return None
        lista_notifiche = []
        if destinatario.get_id() in self._lista_notifiche.keys():
            for notifica in self._lista_notifiche[destinatario.get_id()]:
                lista_notifiche.append(notifica)
        return lista_notifiche

    def get_notifica(self, id_notifica: int):
        for destinatario in self._lista_notifiche.keys():
            for notifica in self._lista_notifiche[destinatario]:
                if notifica.get_id() == id_notifica:
                    return notifica
        return None

    def set_gestori(self, gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori):
        self._gestore_atleti = gestore_atleti
        self._gestore_allenatori = gestore_allenatori

    def set_lista_notifiche(self, lista_notifiche: list[Notifica]):
        for notifica in lista_notifiche:
            destinatario = self._gestore_atleti.get_atleta_per_id(notifica.get_id_destinatario())
            if destinatario is None:
                destinatario = self._gestore_allenatori.get_allenatore_per_id(notifica.get_id_destinatario())
            if destinatario is None:
                continue

            if destinatario in self._lista_notifiche.keys():
                self._lista_notifiche[destinatario].append(notifica)
            else:
                self._lista_notifiche.update({destinatario: [notifica]})

            destinatario.aggiungi_notifica(notifica.get_id())

    def invia_notifica(self, id_destinatario: int, nome_notifica: str, testo: str):
        for destinatario in self._lista_notifiche.keys():
            for notifica in self._lista_notifiche[destinatario]:
                if notifica.get_nome() == nome_notifica:
                    return False

        destinatario = self._gestore_atleti.get_atleta_per_id(id_destinatario)
        if destinatario is None:
            destinatario = self._gestore_allenatori.get_allenatore_per_id(id_destinatario)

        if destinatario is None:
            return False

        nuova_notifica = Notifica(nome_notifica, testo, id_destinatario, datetime.date.today())

        if destinatario in self._lista_notifiche.keys():
            self._lista_notifiche[destinatario].append(nuova_notifica)
        else:
            self._lista_notifiche.update({destinatario: [nuova_notifica]})

        destinatario.aggiungi_notifica(nuova_notifica.get_id())

        return True