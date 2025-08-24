import datetime

from domain.attività.utente import Utente
from domain.servizio.notifica import Notifica

from businnes.GestoreAtleti import GestoreAtleti
from businnes.GestoreAllenatori import GestoreAllenatore

class GestoreNotifiche:

    def __init__(self):
        self._lista_notifiche = {}

    def get_lista_notifiche(self):
        return self._lista_notifiche

    def set_lista_notifiche(self, lista_notifiche: list[Notifica],
                            gestore_atleti: GestoreAtleti,
                            gestore_allenatori: GestoreAllenatore):
        for notifica in lista_notifiche:
            proprietario = gestore_atleti.get_atleta_da_id(notifica.get_id_destinatario())

            if proprietario is None:
                proprietario = gestore_allenatori.get_allenatore_per_id(
                    notifica.get_id_destinatario())

            if proprietario in self._lista_notifiche.keys():
                self._lista_notifiche[proprietario].append(notifica)
            else:
                self._lista_notifiche.update({proprietario: [notifica]})

            proprietario.aggiungi_notifica(notifica)

    def invia_notifica(self, destinatario: Utente, nome_notifica: str, testo: str):
        id_destinatario = destinatario.get_id()
        nuova_notifica = Notifica(nome_notifica, testo, id_destinatario, datetime.date.today().__str__())

        if destinatario in self._lista_notifiche.keys():
            self._lista_notifiche[destinatario].append(nuova_notifica)
        else:
            self._lista_notifiche.update({destinatario: [nuova_notifica]})

        destinatario.aggiungi_notifica(nuova_notifica)