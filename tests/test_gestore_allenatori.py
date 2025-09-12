import unittest
from unittest.mock import Mock

from businnes.gestore_allenatori import GestoreAllenatori
from domain.attività.utente import Utente
from domain.attività.contratto import Contratto

def _crea_dati_allenatore_validi(**overrides):
    """
    Crea un dizionario di dati validi per un allenatore.
    Accetta 'overrides' per modificare campi specifici per ogni test.
    """
    dati_default = {
        "nome": "Denny", "cognome": "Lazzarin", "sesso": "M", "nascita": "1986-01-01",
        "codice_fiscale": "DNNLZR01Z01T198N", "via": "Piazzale della massellanza", "civico": 15, "citta": "Pavia",
        "provincia": "PV", "cap": "20100", "telefono": "3331234567", "email": "danny.lazzarin@dl-gym.com"
    }
    # Applica le modifiche richieste dal test
    dati_default.update(overrides)
    return dati_default

class TestGestoreAllenatori(unittest.TestCase):

    def setUp(self):
        Utente.set_last_id(0)
        Contratto.set_last_id(0)

        self._gestore_atleti = Mock()
        self._gestore_allenatori = GestoreAllenatori(self._gestore_atleti)

        print(f"\n--- Eseguo setUp per il test:  {self.id()} ---")

    def test_aggiungi_allenatore_successo(self):
        dati_allenatore = _crea_dati_allenatore_validi()
        allenatore = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore)

        self.assertIsNotNone(allenatore)
        self.assertEqual(allenatore.get_id(), 1)
        self.assertEqual(allenatore.get_nome(), "Denny")
        self.assertEqual(allenatore.get_cognome(), "Lazzarin")

        lista_allenatori = self._gestore_allenatori.get_lista_allenatori()
        self.assertEqual(Utente.get_last_id(), 1)
        self.assertEqual(len(lista_allenatori), 1)
        self.assertEqual(lista_allenatori[0], allenatore)

    def test_aggiungi_allenatore_email_esistente(self):
        dati_allenatore1 = _crea_dati_allenatore_validi(email="stessaemail@gym.it")
        allenatore1 = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore1)
        self.assertIsNotNone(allenatore1)

        dati_allenatore2 = _crea_dati_allenatore_validi(nome= "Mario", cognome= "Bianchi", email="stessaemail@gym.it", telefono= "3311927199")
        allenatore2 = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore2)
        self.assertIsNone(allenatore2)

        lista_allenatori = self._gestore_allenatori.get_lista_allenatori()
        self.assertEqual(Utente.get_last_id(), 1)
        self.assertEqual(len(lista_allenatori), 1)

    def test_aggiungi_allenatore_telefono_esistente(self):
        dati_allenatore1 = _crea_dati_allenatore_validi(telefono="3311927199")
        allenatore1 = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore1)
        self.assertIsNotNone(allenatore1)

        dati_allenatore2 = _crea_dati_allenatore_validi(nome="Mario", cognome="Bianchi", email="email.diversa@gym.it", telefono="3311927199")
        allenatore2 = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore2)
        self.assertIsNone(allenatore2)

        lista_allenatori = self._gestore_allenatori.get_lista_allenatori()
        self.assertEqual(Utente.get_last_id(), 1)
        self.assertEqual(len(lista_allenatori), 1)

    def test_get_allenatore_per_id_inesistente(self):
        dati_allenatore = _crea_dati_allenatore_validi()
        allenatore_creato = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore)
        self.assertIsNotNone(allenatore_creato)

        allenatore_cercato = self._gestore_allenatori.get_allenatore_per_id(3)
        self.assertIsNone(allenatore_cercato)

    def test_get_allenatore_per_id_successo(self):
        dati_allenatore = _crea_dati_allenatore_validi()
        allenatore_creato = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore)
        self.assertIsNotNone(allenatore_creato)

        allenatore_cercato = self._gestore_allenatori.get_allenatore_per_id(1)
        self.assertIsNotNone(allenatore_cercato)
        self.assertEqual(allenatore_creato, allenatore_cercato)

    def test_get_allenatore_per_nome_inesistente(self):
        dati_allenatore = _crea_dati_allenatore_validi()
        allenatore_creato = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore)
        self.assertIsNotNone(allenatore_creato)

        lista_omonimi = self._gestore_allenatori.get_allenatore_per_nome("Francesco Bagnaia")
        self.assertEqual(lista_omonimi, [])

    def test_get_allenatore_per_nome_successo(self):
        dati_allenatore = _crea_dati_allenatore_validi()
        allenatore_creato = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore)
        self.assertIsNotNone(allenatore_creato)

        lista_omonimi = self._gestore_allenatori.get_allenatore_per_nome("Denny Lazzarin")
        self.assertIsNotNone(lista_omonimi)
        self.assertEqual(allenatore_creato, lista_omonimi[0])

    def test_assegna_atleta_ad_allenatore_successo(self):
        dati_allenatore = _crea_dati_allenatore_validi()
        allenatore = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore)
        self.assertIsNotNone(allenatore)

        atleta_finto = Mock()
        atleta_finto.get_id.return_value = 1
        self._gestore_atleti.get_atleta_per_id.return_value = atleta_finto

        contratto = self._gestore_allenatori.assegna_atleta_ad_allenatore(allenatore.get_id(), 1)
        self.assertIsNotNone(contratto)
        self.assertEqual(contratto.get_id(), 1)
        self.assertEqual(contratto.get_id_atleta(), atleta_finto.get_id())
        self.assertEqual(contratto.get_id_allenatore(), allenatore.get_id())

        lista_contratti = self._gestore_allenatori.get_lista_contratti()
        self.assertEqual(len(lista_contratti), 1)
        self.assertEqual(lista_contratti[0], contratto)

        lista_atleti = allenatore.get_lista_atleti()
        self.assertEqual(len(lista_atleti), 1)
        self.assertEqual(lista_atleti[0], contratto.get_id())
        atleta_finto.assegna_allenatore.assert_called_once_with(contratto.get_id())

    def test_assegna_atleta_ad_allenatore_atleta_inesistente(self):
        dati_allenatore = _crea_dati_allenatore_validi()
        allenatore = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore)
        self.assertIsNotNone(allenatore)

        self._gestore_atleti.get_atleta_per_id.return_value = None

        contratto = self._gestore_allenatori.assegna_atleta_ad_allenatore(allenatore.get_id(), 10)
        self.assertIsNone(contratto)

    def test_assegna_atleta_ad_allenatore_allenatore_non_esistente(self):
        dati_allenatore = _crea_dati_allenatore_validi()
        allenatore = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore)
        self.assertIsNotNone(allenatore)

        atleta_finto = Mock()
        self._gestore_atleti.get_atleta_per_id.return_value = atleta_finto
        atleta_finto.get_id.return_value = 1

        contratto = self._gestore_allenatori.assegna_atleta_ad_allenatore(2, 1)
        self.assertIsNone(contratto)

    def test_assegna_atleta_ad_allenatore_atleta_gia_assegnato(self):
        dati_allenatore = _crea_dati_allenatore_validi()
        allenatore = self._gestore_allenatori.aggiungi_allenatore(**dati_allenatore)
        self.assertIsNotNone(allenatore)

        atleta_finto = Mock()
        self._gestore_atleti.get_atleta_per_id.return_value = atleta_finto
        atleta_finto.get_id.return_value = 1

        primo_tentativo = self._gestore_allenatori.assegna_atleta_ad_allenatore(1, 1)
        self.assertIsNotNone(primo_tentativo)

        secondo_tentativo = self._gestore_allenatori.assegna_atleta_ad_allenatore(1, 1)
        self.assertIsNone(secondo_tentativo)