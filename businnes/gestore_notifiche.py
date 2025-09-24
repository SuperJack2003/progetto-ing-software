import datetime
from typing import Optional

from domain.servizio.notifica import Notifica
from domain.attività.utente import Utente

from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori

class GestoreNotifiche:

    def __init__(self, gestore_atleti: GestoreAtleti, gestore_allenatori: GestoreAllenatori):
        self._notifiche_per_id = {}

        self._gestore_atleti = gestore_atleti
        self._gestore_allenatori = gestore_allenatori

    def _trova_destinatario(self, id_destinatario: int) -> Optional[Utente]:
        destinatario = self._gestore_atleti.get_atleta_per_id(id_destinatario)
        if destinatario is None:
            destinatario = self._gestore_allenatori.get_allenatore_per_id(id_destinatario)

        return destinatario

    def get_lista_notifiche(self):
        return list(self._notifiche_per_id.values())

    def get_notifiche_da_utente(self, id_destinatario: int) -> Optional[list[Notifica]]:
        destinatario = self._trova_destinatario(id_destinatario)
        if destinatario:
            return [notifica for notifica in self._notifiche_per_id.values() if notifica.get_id_destinatario() == id_destinatario]
        else: return []

    def get_notifica(self, id_notifica: int):
        return self._notifiche_per_id.get(id_notifica)

    def carica_notifiche(self, lista_notifiche: list[Notifica]):
        self._notifiche_per_id = {notifica.get_id(): notifica for notifica in lista_notifiche}

    def invia_notifica(self, id_destinatario: int, nome_notifica: str, testo: str, data_opzionale: Optional[datetime.date] = None) -> Optional[Notifica]:
        for notifica in self._notifiche_per_id.values():
            if notifica.get_nome() == nome_notifica and notifica.get_id_destinatario() == id_destinatario:
                return None

        destinatario = self._trova_destinatario(id_destinatario)
        if not destinatario:
            return None

        data_inizio = data_opzionale if data_opzionale is not None else datetime.date.today()
        nuova_notifica = Notifica(nome_notifica, testo, id_destinatario, data_inizio)
        self._notifiche_per_id.update({nuova_notifica.get_id(): nuova_notifica})
        destinatario.aggiungi_notifica(nuova_notifica.get_id())

        return nuova_notifica