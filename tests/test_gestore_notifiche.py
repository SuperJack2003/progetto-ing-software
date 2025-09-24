import unittest
from unittest.mock import Mock

from domain.servizio.notifica import Notifica

from businnes.gestore_notifiche import GestoreNotifiche

def _crea_dati_notifica(**overrides):
    dati_default = {
        "nome_notifica": "Notifica scadenza abbonamento", "testo": "Si notifica che il suo abbonamento è in scadenza", "data_opzionale": None,
    }
    dati_default.update(overrides)
    return dati_default

class TestGestoreNotifiche(unittest.TestCase):

    def setUp(self):
        Notifica.set_last_id(0)

        self._gestore_allenatori = Mock()
        self._gestore_atleti =  Mock()
        self._gestore_notifiche = GestoreNotifiche(self._gestore_atleti, self._gestore_allenatori)

    def test_invia_notifica_atleta_successo(self):
        dati_notifica = _crea_dati_notifica()

        atleta = Mock()
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        nuova_notifica = self._gestore_notifiche.invia_notifica(1, **dati_notifica)
        self.assertIsNotNone(nuova_notifica)
        self.assertEqual(nuova_notifica.get_id(), 1)
        self.assertEqual(nuova_notifica.get_id_destinatario(), 1)
        self.assertEqual(nuova_notifica.get_nome(), "Notifica scadenza abbonamento")

        lista_notifiche = self._gestore_notifiche.get_lista_notifiche()
        self.assertEqual(len(lista_notifiche), 1)
        self.assertEqual(lista_notifiche[0], nuova_notifica)
        self.assertEqual(Notifica.get_last_id(), 1)

        atleta.aggiungi_notifica.assert_called_once_with(nuova_notifica.get_id())

    def test_invia_notifica_allenatore_successo(self):
        dati_notifica = _crea_dati_notifica()

        allenatore = Mock()
        self._gestore_atleti.get_atleta_per_id.return_value = None
        self._gestore_allenatori.get_allenatore_per_id.return_value = allenatore

        nuova_notifica = self._gestore_notifiche.invia_notifica(3, **dati_notifica)
        self.assertIsNotNone(nuova_notifica)
        self.assertEqual(nuova_notifica.get_id(), 1)
        self.assertEqual(nuova_notifica.get_id_destinatario(), 3)
        self.assertEqual(nuova_notifica.get_nome(), "Notifica scadenza abbonamento")

        lista_notifiche = self._gestore_notifiche.get_lista_notifiche()
        self.assertEqual(len(lista_notifiche), 1)
        self.assertEqual(lista_notifiche[0], nuova_notifica)
        self.assertEqual(Notifica.get_last_id(), 1)

        allenatore.aggiungi_notifica.assert_called_once_with(nuova_notifica.get_id())

    def test_invia_notifica_gia_esistente(self):
        dati_notifica = _crea_dati_notifica()

        atleta = Mock()
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        notifica1 = self._gestore_notifiche.invia_notifica(1, **dati_notifica)
        self.assertIsNotNone(notifica1)

        notifica2 = self._gestore_notifiche.invia_notifica(1, **dati_notifica)
        self.assertIsNone(notifica2)

        lista_notifiche = self._gestore_notifiche.get_lista_notifiche()
        self.assertEqual(len(lista_notifiche), 1)
        self.assertEqual(Notifica.get_last_id(), 1)

    def test_invia_notifica_destinatario_inesistente(self):
        dati_notifica = _crea_dati_notifica()

        self._gestore_atleti.get_atleta_per_id.return_value = None
        self._gestore_allenatori.get_allenatore_per_id.return_value = None

        nuova_notifica = self._gestore_notifiche.invia_notifica(1, **dati_notifica)
        self.assertIsNone(nuova_notifica)

    def test_invia_notifiche_multiple(self):
        dati_notifica1 = _crea_dati_notifica()
        dati_notifica2 = _crea_dati_notifica(nome_notifica="Avviso cancellazione corso: Karate")

        atleta = Mock()
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        notifica1 = self._gestore_notifiche.invia_notifica(1, **dati_notifica1)
        self.assertIsNotNone(notifica1)
        notifica2 = self._gestore_notifiche.invia_notifica(1, **dati_notifica2)
        self.assertIsNotNone(notifica2)

        lista_notifiche = self._gestore_notifiche.get_lista_notifiche()
        self.assertEqual(len(lista_notifiche), 2)
        self.assertEqual(lista_notifiche[0], notifica1)
        self.assertEqual(lista_notifiche[1], notifica2)
        self.assertEqual(Notifica.get_last_id(), 2)

    def test_get_notifiche_da_utente_nessuna_notifica(self):
        dati_notifica = _crea_dati_notifica()

        atleta = Mock()
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        nuova_notifica = self._gestore_notifiche.invia_notifica(1, **dati_notifica)
        self.assertIsNotNone(nuova_notifica)

        lista_notifiche_utente = self._gestore_notifiche.get_notifiche_da_utente(2)
        self.assertEqual(lista_notifiche_utente, [])

    def test_get_notifiche_da_utente_successo(self):
        dati_notifica1 = _crea_dati_notifica()
        dati_notifica2 = _crea_dati_notifica(nome_notifica="Avviso cancellazione corso: Karate")

        atleta = Mock()
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        notifica1 = self._gestore_notifiche.invia_notifica(1, **dati_notifica1)
        self.assertIsNotNone(notifica1)
        notifica2 = self._gestore_notifiche.invia_notifica(1, **dati_notifica2)
        self.assertIsNotNone(notifica2)

        lista_notifiche_utente = self._gestore_notifiche.get_notifiche_da_utente(1)
        self.assertEqual(len(lista_notifiche_utente), 2)
        self.assertEqual(lista_notifiche_utente[0], notifica1)
        self.assertEqual(lista_notifiche_utente[1], notifica2)