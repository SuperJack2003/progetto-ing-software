import unittest
from unittest.mock import Mock, patch
import datetime

from domain.attività.atleta import Atleta
from domain.attività.allenatore import Allenatore

from domain.servizio.corso import Corso
from domain.attività.contratto import Contratto

from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_allenatori import GestoreAllenatori
from businnes.gestore_corsi import GestoreCorsi

def _crea_dati_corso(**override):
    dati_default = {
        "nome": "Karate Adulti",
        "descrizione": "Corso di Karate per adulti",
        "eta_min": 16,
        "eta_max": 99,
        "orari_corso": "Lunedì 19-20, Mercoledì 18-20, Venerdì 19-20"
    }
    dati_default.update(override)
    return dati_default

class TestGestoreCorsi(unittest.TestCase):

    def setUp(self):
        Corso.set_last_id(0)
        Contratto.set_last_id(0)

        self._gestore_atleti = Mock(spec=GestoreAtleti)
        self._gestore_allenatori = Mock(spec=GestoreAllenatori)
        self._gestore_corsi = GestoreCorsi(self._gestore_atleti, self._gestore_allenatori)

        print(f"\n--- Eseguo setUp per il test:  {self.id()} ---")

    def test_aggiungi_corso_successo(self):
        dati_corso = _crea_dati_corso()

        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)
        self.assertEqual(corso.get_id(), 1)
        self.assertEqual(corso.get_nome(), "Karate Adulti")
        self.assertEqual(corso.get_programmazione_settimanale().__str__(), "Lunedì 19-20, Mercoledì 18-20, Venerdì 19-20")

        lista_corsi = self._gestore_corsi.get_lista_corsi()
        self.assertEqual(len(lista_corsi), 1)
        self.assertEqual(lista_corsi[0], corso)
        self.assertEqual(Corso.get_last_id(), 1)

    def test_aggiungi_corso_gia_esistente(self):
        dati_corso1 = _crea_dati_corso()
        dati_corso2 = _crea_dati_corso(descrizione = "Corso duplicato")

        corso1 = self._gestore_corsi.aggiungi_corso(**dati_corso1)
        self.assertIsNotNone(corso1)

        corso2 = self._gestore_corsi.aggiungi_corso(**dati_corso2)
        self.assertIsNone(corso2)

        lista_corsi = self._gestore_corsi.get_lista_corsi()
        self.assertEqual(len(lista_corsi), 1)
        self.assertEqual(lista_corsi[0], corso1)
        self.assertEqual(Corso.get_last_id(), 1)

    def test_aggiungi_corsi_multipli(self):
        dati_corso1 = _crea_dati_corso()
        dati_corso2 = _crea_dati_corso(nome="Ginnastica leggera", orari_corso="Martedì 9-10, Giovedì 9-10, Sabato 9-10")

        corso1 = self._gestore_corsi.aggiungi_corso(**dati_corso1)
        self.assertIsNotNone(corso1)

        corso2 = self._gestore_corsi.aggiungi_corso(**dati_corso2)
        self.assertIsNotNone(corso2)

        lista_corsi = self._gestore_corsi.get_lista_corsi()
        self.assertEqual(len(lista_corsi), 2)
        self.assertEqual(lista_corsi[0], corso1)
        self.assertEqual(lista_corsi[1], corso2)
        self.assertEqual(Corso.get_last_id(), 2)

    @patch("businnes.gestore_corsi.datetime")
    def test_get_corsi_in_partenza_nessun_corso(self, mock_datetime):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        mock_datetime.date.today.return_value = datetime.date(2025, 9, 26)
        mock_datetime.timedelta = datetime.timedelta

        corsi_in_partenza = self._gestore_corsi.get_corsi_in_partenza()
        self.assertEqual(corsi_in_partenza, [])

    @patch("businnes.gestore_corsi.datetime")
    def test_get_corsi_in_partenza_successo(self, mock_datetime):
        dati_corso1 = _crea_dati_corso()
        dati_corso2 = _crea_dati_corso(
            nome = "Ginnastica leggera", orari_corso= "Martedì 9-10, Giovedì 9-10, Sabato 9-10"
        )

        corso1 = self._gestore_corsi.aggiungi_corso(**dati_corso1)
        self.assertIsNotNone(corso1)

        corso2 = self._gestore_corsi.aggiungi_corso(**dati_corso2)
        self.assertIsNotNone(corso2)

        mock_datetime.date.today.return_value = datetime.date(2025, 9, 26)
        mock_datetime.timedelta = datetime.timedelta

        corsi_in_partenza = self._gestore_corsi.get_corsi_in_partenza()
        self.assertEqual(len(corsi_in_partenza), 1)
        self.assertEqual(corsi_in_partenza[0], corso2)

    def test_set_stato_corso_inesistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        risultato = self._gestore_corsi.set_stato_corso(2, False)
        self.assertEqual(risultato, False)
        self.assertEqual(corso.get_stato(), True)

    def test_set_stato_corso_successo(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        risultato = self._gestore_corsi.set_stato_corso(1, False)
        self.assertEqual(risultato, True)
        self.assertEqual(corso.get_stato(), False)

    def test_iscrivi_atleta_successo(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta
        atleta.get_eta.return_value = 22

        contratto = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNotNone(contratto)
        self.assertEqual(contratto.get_id(), 1)
        self.assertEqual(contratto.get_id_atleta(), 1)
        self.assertEqual(contratto.get_id_corso(), 1)
        self.assertEqual(contratto.get_data(), datetime.date.today())
        atleta.aggiungi_iscrizione.assert_called_once_with(contratto.get_id())

        lista_contratti = self._gestore_corsi.get_lista_contratti_atleti()
        self.assertEqual(len(lista_contratti), 1)
        self.assertEqual(lista_contratti[0], contratto)
        self.assertEqual(Contratto.get_last_id(), 1)

    def test_iscrivi_atleta_corso_inesistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta
        atleta.get_eta.return_value = 22

        contratto = self._gestore_corsi.iscrivi_atleta(1, 2)
        self.assertIsNone(contratto)

        lista_contratti = self._gestore_corsi.get_lista_contratti_atleti()
        self.assertEqual(lista_contratti, [])
        self.assertEqual(Contratto.get_last_id(), 0)

    def test_iscrivi_atleta_inesistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        self._gestore_atleti.get_atleta_per_id.return_value = None

        contratto = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNone(contratto)

        lista_contratti = self._gestore_corsi.get_lista_contratti_atleti()
        self.assertEqual(lista_contratti, [])
        self.assertEqual(Contratto.get_last_id(), 0)

    def test_iscrivi_atleta_gia_iscritto(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta
        atleta.get_eta.return_value = 22

        contratto1 = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNotNone(contratto1)

        contratto2 = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNone(contratto2)

        lista_contratti = self._gestore_corsi.get_lista_contratti_atleti()
        self.assertEqual(len(lista_contratti), 1)
        self.assertEqual(lista_contratti[0], contratto1)
        self.assertEqual(Contratto.get_last_id(), 1)

    def test_iscrivi_atleti_eta_non_valida(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta
        atleta.get_eta.return_value = 12

        contratto = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNone(contratto)

        lista_contratti = self._gestore_corsi.get_lista_contratti_atleti()
        self.assertEqual(lista_contratti, [])
        self.assertEqual(Contratto.get_last_id(), 0)

    def test_iscrivi_atleti_multipli(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        atleta1 = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta1
        atleta1.get_eta.return_value = 22

        contratto1 = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNotNone(contratto1)
        atleta1.aggiungi_iscrizione.assert_called_once_with(contratto1.get_id())

        atleta2 = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta2
        atleta2.get_eta.return_value = 16

        contratto2 = self._gestore_corsi.iscrivi_atleta(2, 1)
        self.assertIsNotNone(contratto2)
        atleta2.aggiungi_iscrizione.assert_called_once_with(contratto2.get_id())

        lista_contratti = self._gestore_corsi.get_lista_contratti_atleti()
        self.assertEqual(len(lista_contratti), 2)
        self.assertEqual(lista_contratti[0], contratto1)
        self.assertEqual(lista_contratti[1], contratto2)
        self.assertEqual(Contratto.get_last_id(), 2)

    def test_get_iscritti_corso_inesistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta
        atleta.get_eta.return_value = 12

        contratto = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNone(contratto)

        lista_iscritti = self._gestore_corsi.get_iscritti_corso(2)
        self.assertEqual(lista_iscritti, [])

    def test_get_iscritti_corso_successo(self):
        dati_corso1 = _crea_dati_corso()
        dati_corso2 = _crea_dati_corso(nome="Ginnastica leggera", orari_corso="Martedì 9-10, Giovedì 9-10, Sabato 9-10")

        corso1 = self._gestore_corsi.aggiungi_corso(**dati_corso1)
        self.assertIsNotNone(corso1)

        corso2 = self._gestore_corsi.aggiungi_corso(**dati_corso2)
        self.assertIsNotNone(corso2)

        atleta1 = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta1
        atleta1.get_eta.return_value = 22

        contratto1 = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNotNone(contratto1)

        atleta2 = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta2
        atleta2.get_eta.return_value = 70

        contratto2 = self._gestore_corsi.iscrivi_atleta(2, 2)
        self.assertIsNotNone(contratto2)

        lista_iscritti = self._gestore_corsi.get_iscritti_corso(1)
        self.assertEqual(len(lista_iscritti), 1)
        self.assertEqual(lista_iscritti[0].get_id(), 1)

    def test_get_contratti_atleta_inesistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta
        atleta.get_eta.return_value = 22

        contratto = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNotNone(contratto)

        contratti_atleta = self._gestore_corsi.get_contratti_atleta(2)
        self.assertEqual(contratti_atleta, [])

    def test_get_contratti_atleta_successo(self):
        dati_corso1 = _crea_dati_corso()
        dati_corso2 = _crea_dati_corso(nome="Ginnastica leggera", orari_corso="Martedì 9-10, Giovedì 9-10, Sabato 9-10")

        corso1 = self._gestore_corsi.aggiungi_corso(**dati_corso1)
        self.assertIsNotNone(corso1)

        corso2 = self._gestore_corsi.aggiungi_corso(**dati_corso2)
        self.assertIsNotNone(corso2)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta
        atleta.get_eta.return_value = 22

        contratto1 = self._gestore_corsi.iscrivi_atleta(1, 1)
        self.assertIsNotNone(contratto1)

        contratto2 = self._gestore_corsi.iscrivi_atleta(1, 2)
        self.assertIsNotNone(contratto2)

        contratti_atleta = self._gestore_corsi.get_contratti_atleta(1)
        self.assertEqual(len(contratti_atleta), 2)
        self.assertEqual(contratti_atleta[0].get_id_corso(), corso1.get_id())
        self.assertEqual(contratti_atleta[1].get_id_corso(), corso2.get_id())

    def test_assegna_allenatore_successo(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        allenatore = Mock(spec=Allenatore)
        self._gestore_allenatori.get_allenatore_per_id.return_value = allenatore

        contratto = self._gestore_corsi.assegna_allenatore(1, 1)
        self.assertIsNotNone(contratto)
        self.assertEqual(contratto.get_id(), 1)
        self.assertEqual(contratto.get_id_corso(), corso.get_id())
        self.assertEqual(contratto.get_id_allenatore(), 1)
        allenatore.aggiungi_corso.assert_called_once_with(contratto.get_id())

        lista_contratti = self._gestore_corsi.get_lista_contratti_allenatori()
        self.assertEqual(len(lista_contratti), 1)
        self.assertEqual(lista_contratti[0], contratto)
        self.assertEqual(Contratto.get_last_id(), 1)

    def test_assegna_allenatore_inesistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        self._gestore_allenatori.get_allenatore_per_id.return_value = None

        contratto = self._gestore_corsi.assegna_allenatore(1, 1)
        self.assertIsNone(contratto)

        lista_contratti = self._gestore_corsi.get_lista_contratti_allenatori()
        self.assertEqual(lista_contratti, [])
        self.assertEqual(Contratto.get_last_id(), 0)

    def test_assegna_allenatore_corso_inesistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        allenatore = Mock(spec=Allenatore)
        self._gestore_allenatori.get_allenatore_per_id.return_value = allenatore

        contratto = self._gestore_corsi.assegna_allenatore(1, 2)
        self.assertIsNone(contratto)

        lista_contratti = self._gestore_corsi.get_lista_contratti_allenatori()
        self.assertEqual(lista_contratti, [])
        self.assertEqual(Contratto.get_last_id(), 0)

    def test_assegna_allenatore_contratto_esistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        allenatore = Mock(spec=Allenatore)
        self._gestore_allenatori.get_allenatore_per_id.return_value = allenatore

        contratto1 = self._gestore_corsi.assegna_allenatore(1, 1)
        self.assertIsNotNone(contratto1)

        contratto2 = self._gestore_corsi.assegna_allenatore(1, 1)
        self.assertIsNone(contratto2)

        lista_corsi = self._gestore_corsi.get_lista_contratti_allenatori()
        self.assertEqual(len(lista_corsi), 1)
        self.assertEqual(Contratto.get_last_id(), 1)

    def test_get_allenatore_corso_non_ha_allenatore(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        contratto_allenatore = self._gestore_corsi.get_allenatore_corso(1)
        self.assertIsNone(contratto_allenatore)

    def test_get_allenatore_corso_inesistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        allenatore = Mock(spec=Allenatore)
        self._gestore_allenatori.get_allenatore_per_id.return_value = allenatore

        contratto = self._gestore_corsi.assegna_allenatore(1, 1)
        self.assertIsNotNone(contratto)

        contratto_allenatore = self._gestore_corsi.get_allenatore_corso(2)
        self.assertIsNone(contratto_allenatore)

    def test_get_allenatore_corso_successo(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        allenatore = Mock(spec=Allenatore)
        self._gestore_allenatori.get_allenatore_per_id.return_value = allenatore

        contratto = self._gestore_corsi.assegna_allenatore(1, 1)
        self.assertIsNotNone(contratto)

        contratto_allenatore = self._gestore_corsi.get_allenatore_corso(1)
        self.assertEqual(contratto_allenatore.get_id_allenatore(), 1)

    def test_get_contratti_allenatore_inesistente(self):
        dati_corso = _crea_dati_corso()
        corso = self._gestore_corsi.aggiungi_corso(**dati_corso)
        self.assertIsNotNone(corso)

        self._gestore_allenatori.get_allenatore_per_id.return_value = None

        contratti_allenatore = self._gestore_corsi.get_contratti_allenatore(1)
        self.assertEqual(contratti_allenatore, [])

    def test_get_contratti_allenatore_successo(self):
        dati_corso1 = _crea_dati_corso()
        dati_corso2 = _crea_dati_corso(nome="Ginnastica Leggera")
        corso1 = self._gestore_corsi.aggiungi_corso(**dati_corso1)
        corso2 = self._gestore_corsi.aggiungi_corso(**dati_corso2)
        self.assertIsNotNone(corso1)
        self.assertIsNotNone(corso2)

        allenatore = Mock(spec=Allenatore)
        self._gestore_allenatori.get_allenatore_per_id.return_value = allenatore

        contratto1 = self._gestore_corsi.assegna_allenatore(1, 2)
        self.assertIsNotNone(contratto1)

        contratti_allenatore = self._gestore_corsi.get_contratti_allenatore(1)
        self.assertEqual(len(contratti_allenatore), 1)
        self.assertEqual(contratti_allenatore[0].get_id_corso(), corso2.get_id())