import unittest

from businnes.gestore_atleti import GestoreAtleti
from domain.attività.utente import Utente


def _crea_dati_atleta_validi(**overrides):
    """
    Crea un dizionario di dati validi per un atleta.
    Accetta 'overrides' per modificare campi specifici per ogni test.
    """
    dati_default = {
        "nome": "Mario", "cognome": "Rossi", "sesso": "M", "nascita": "1999-01-01",
        "codice_fiscale": "MRORSS99A01H501U", "via": "Via Roma", "civico": 1, "citta": "Roma",
        "provincia": "RM", "cap": "00100", "telefono": "3331234567", "email": "mario.rossi@gym.com"
    }
    # Applica le modifiche richieste dal test
    dati_default.update(overrides)
    return dati_default


class TestGestoreAtleti(unittest.TestCase):

    def setUp(self):
        Utente.set_last_id(0)

        self._gestore_atleti = GestoreAtleti()

        print(f"\n--- Eseguo setUp per il test:  {self.id()} ---")

    def test_crea_nuovo_atleta_successo(self):
        dati_atleta = _crea_dati_atleta_validi()

        atleta = self._gestore_atleti.aggiungi_atleta(**dati_atleta)

        self.assertIsNotNone(atleta)
        self.assertEqual(atleta.get_id(), 1)
        self.assertEqual(atleta.get_nome(), "Mario")
        self.assertEqual(atleta.get_cognome(), "Rossi")

        lista_atleti = self._gestore_atleti.get_lista_atleti()
        self.assertEqual(len(lista_atleti), 1)
        self.assertEqual(lista_atleti[0], atleta)

    def test_crea_nuovo_atleta_email_esistente(self):
        dati_primo_atleta = _crea_dati_atleta_validi(email="stessa.email@gym.com")
        primo_atleta = self._gestore_atleti.aggiungi_atleta(**dati_primo_atleta)
        self.assertIsNotNone(primo_atleta)

        dati_secondo_atleta = _crea_dati_atleta_validi(
            nome="Luigi", cognome="Verdi", email="stessa.email@gym.com"
        )

        secondo_atleta = self._gestore_atleti.aggiungi_atleta(**dati_secondo_atleta)

        self.assertIsNone(secondo_atleta, "L'atleta è nullo perché con email uguale ad un'altro già esistente")
        lista_atleti = self._gestore_atleti.get_lista_atleti()
        self.assertEqual(len(lista_atleti), 1)

    def test_crea_nuovo_atleta_telefono_esistente(self):
        dati_primo_atleta = _crea_dati_atleta_validi(telefono="3339876543")
        primo_atleta = self._gestore_atleti.aggiungi_atleta(**dati_primo_atleta)
        self.assertIsNotNone(primo_atleta)

        dati_secondo_atleta = _crea_dati_atleta_validi(
            nome="Luigi", email="luigi.verdi@gym.com", telefono="3339876543"
        )

        secondo_atleta = self._gestore_atleti.aggiungi_atleta(**dati_secondo_atleta)

        self.assertIsNone(secondo_atleta, "L'atleta è nullo perché con telefono uguale ad un'altro già esistente")
        lista_atleti = self._gestore_atleti.get_lista_atleti()
        self.assertEqual(len(lista_atleti), 1)

    def test_get_atleta_per_id_non_esistente(self):
        atleta = self._gestore_atleti.get_atleta_per_id(3)

        self.assertIsNone(atleta)

    def test_get_atleta_per_id_successo(self):
        dati_atleta = _crea_dati_atleta_validi()
        self._gestore_atleti.aggiungi_atleta(**dati_atleta)

        atleta = self._gestore_atleti.get_atleta_per_id(1)
        self.assertIsNotNone(atleta)
        self.assertEqual(atleta.get_id(), 1)
        self.assertEqual(atleta.get_nome(), "Mario")
        self.assertEqual(atleta.get_cognome(), "Rossi")

    def test_get_atleta_per_nome_non_esistente(self):
        atleta = self._gestore_atleti.get_atleta_per_nome("Mario Rossi")

        self.assertIsNotNone(atleta)
        self.assertEqual(atleta, [])

    def test_get_atleta_per_nome_successo(self):
        dati_atleta = _crea_dati_atleta_validi()
        self._gestore_atleti.aggiungi_atleta(**dati_atleta)

        atleta = self._gestore_atleti.get_atleta_per_nome("Mario Rossi")
        self.assertIsNotNone(atleta)
        self.assertEqual(len(atleta), 1)
        self.assertEqual(atleta[0].get_nome(), "Mario")