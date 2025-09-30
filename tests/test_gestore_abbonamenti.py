import unittest
from unittest.mock import Mock
import datetime
from dateutil import relativedelta

from domain.attività.contratto import Contratto
from domain.attività.atleta import Atleta

from domain.servizio.abbonamento import Abbonamento

from businnes.gestore_atleti import GestoreAtleti
from businnes.gestore_abbonamenti import GestoreAbbonamenti

def _crea_dati_abbonamento(**overrides):
    dati_default = {
        "durata": 4, "tipo": "corsi+sala"
    }
    dati_default.update(overrides)
    return dati_default

class TestGestoreAbbonamenti(unittest.TestCase):

    def setUp(self):
        Abbonamento.set_last_id(0)
        Contratto.set_last_id(0)

        self._gestore_atleti = Mock(spec=GestoreAtleti)
        self._gestore_abbonamenti = GestoreAbbonamenti(self._gestore_atleti)

        print(f"\n--- Eseguo setUp per il test:  {self.id()} ---")

    def test_crea_abbonamento_successo(self):
        dati_abbonamento = _crea_dati_abbonamento()

        abbonamento_creato = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento_creato)
        self.assertEqual(abbonamento_creato.get_id(), 1)
        self.assertEqual(abbonamento_creato.get_nome(), "4-corsi+sala")

        lista_abbonamenti = self._gestore_abbonamenti.get_lista_abbonamenti()
        self.assertEqual(len(lista_abbonamenti), 1)
        self.assertEqual(lista_abbonamenti[0], abbonamento_creato)

    def test_crea_abbonamento_gia_esistente(self):
        dati_abbonamento = _crea_dati_abbonamento()

        abbonamento1 = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento1)

        abbonamento2 = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNone(abbonamento2)

        lista_abbonamenti = self._gestore_abbonamenti.get_lista_abbonamenti()
        self.assertEqual(len(lista_abbonamenti), 1)
        self.assertEqual(Abbonamento.get_last_id(), 1)

    def test_crea_abbonamenti_multipli(self):
        dati_abbonamento1 = _crea_dati_abbonamento()
        abbonamento1 = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento1)
        self.assertIsNotNone(abbonamento1)

        dati_abbonamento2 = _crea_dati_abbonamento(tipo="corsi")
        abbonamento2 = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento2)
        self.assertIsNotNone(abbonamento2)

        dati_abbonamento3 = _crea_dati_abbonamento(durata=2)
        abbonamento3 = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento3)
        self.assertIsNotNone(abbonamento3)

        lista_abbonamenti = self._gestore_abbonamenti.get_lista_abbonamenti()
        self.assertEqual(len(lista_abbonamenti), 3)
        self.assertEqual(Abbonamento.get_last_id(), 3)

    def test_get_abbonamento_per_id_non_esistente(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        abbonamento_cercato = self._gestore_abbonamenti.get_abbonamento_per_id(3)
        self.assertIsNone(abbonamento_cercato)

    def test_get_abbonamento_per_id_successo(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        abbonamento_cercato = self._gestore_abbonamenti.get_abbonamento_per_id(1)
        self.assertIsNotNone(abbonamento_cercato)
        self.assertEqual(abbonamento_cercato, abbonamento)

    def test_crea_contratto_successo(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNotNone(contratto)
        self.assertEqual(contratto.get_id(), 1)
        self.assertEqual(contratto.get_id_abbonamento(), 1)
        self._gestore_atleti.get_atleta_per_id.assert_called_once_with(1)
        atleta.assegna_abbonamento.assert_called_once_with(contratto.get_id())

        lista_contratti = self._gestore_abbonamenti.get_lista_contratti()
        self.assertEqual(len(lista_contratti), 1)
        self.assertEqual(lista_contratti[0], contratto)
        self.assertEqual(Contratto.get_last_id(), 1)

    def test_crea_contratto_atleta_inesistente(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        self._gestore_atleti.get_atleta_per_id.return_value = None

        contratto = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNone(contratto)

        lista_contratti = self._gestore_abbonamenti.get_lista_contratti()
        self.assertEqual(lista_contratti, [])

    def test_crea_contratto_abbonamento_inesistente(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto = self._gestore_abbonamenti.crea_contratto(1, 3)
        self.assertIsNone(contratto)

        lista_contratti = self._gestore_abbonamenti.get_lista_contratti()
        self.assertEqual(lista_contratti, [])

    def test_crea_contratto_gia_esistente(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto1 = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNotNone(contratto1)

        contratto2 = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNone(contratto2)

        lista_contratti = self._gestore_abbonamenti.get_lista_contratti()
        self.assertEqual(len(lista_contratti), 1)
        self.assertEqual(Contratto.get_last_id(), 1)

    def test_get_contratto_per_id_inesistente(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNotNone(contratto)

        contratto_cercato = self._gestore_abbonamenti.get_contratto_per_id(3)
        self.assertIsNone(contratto_cercato)

    def test_get_contratto_per_id_successo(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNotNone(contratto)

        contratto_cercato = self._gestore_abbonamenti.get_contratto_per_id(1)
        self.assertIsNotNone(contratto_cercato)
        self.assertEqual(contratto_cercato, contratto)

    def test_get_contratto_atleta_inesistente(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNotNone(contratto)

        contratto_cercato = self._gestore_abbonamenti.get_contratto_atleta(3)
        self.assertIsNone(contratto_cercato)

    def test_get_contratto_atleta_successo(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNotNone(contratto)

        contratto_cercato = self._gestore_abbonamenti.get_contratto_atleta(1)
        self.assertIsNotNone(contratto_cercato)
        self.assertEqual(contratto_cercato, contratto)

    def test_controllo_scadenze_nessun_contratto_in_scadenza(self):
        dati_abbonamento = _crea_dati_abbonamento()
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNotNone(contratto)

        contratti_in_scadenza = self._gestore_abbonamenti.controllo_scadenze()
        self.assertEqual(contratti_in_scadenza, [])

    def test_controllo_scadenze_successo(self):
        dati_abbonamento1 = _crea_dati_abbonamento(durata=1)
        abbonamento1 = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento1)
        self.assertIsNotNone(abbonamento1)

        dati_abbonamento2 = _crea_dati_abbonamento()
        abbonamento2 = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento2)
        self.assertIsNotNone(abbonamento2)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        data_contratto1 = (datetime.date.today() + datetime.timedelta(days=1)) - relativedelta.relativedelta(months=1)
        contratto1 = self._gestore_abbonamenti.crea_contratto(1, 1, data_contratto1)
        self.assertIsNotNone(contratto1)

        contratto2 = self._gestore_abbonamenti.crea_contratto(2, 2)
        self.assertIsNotNone(contratto2)

        contratti_in_scadenza = self._gestore_abbonamenti.controllo_scadenze()
        self.assertEqual(len(contratti_in_scadenza), 1)
        self.assertEqual(contratti_in_scadenza[0], contratto1)

    def test_controllo_tipo_abbonamento(self):
        dati_abbonamento1 = _crea_dati_abbonamento()
        abbonamento1 = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento1)
        self.assertIsNotNone(abbonamento1)

        dati_abbonamento2 = _crea_dati_abbonamento(tipo="corsi")
        abbonamento2 = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento2)
        self.assertIsNotNone(abbonamento2)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto1 = self._gestore_abbonamenti.crea_contratto(1, 1)
        self.assertIsNotNone(contratto1)

        contratto2 = self._gestore_abbonamenti.crea_contratto(2, 2)
        self.assertIsNotNone(contratto2)

        controllo1 = self._gestore_abbonamenti.controllo_tipo_abbonamento(1, "corsi+sala")
        controllo2 = self._gestore_abbonamenti.controllo_tipo_abbonamento(1, "corsi")
        controllo3 = self._gestore_abbonamenti.controllo_tipo_abbonamento(2, "corsi+sala")
        controllo4 = self._gestore_abbonamenti.controllo_tipo_abbonamento(2, "corsi")
        self.assertEqual(controllo1, True)
        self.assertEqual(controllo2, False)
        self.assertEqual(controllo3, False)
        self.assertEqual(controllo4, True)

    def test_controllo_abbonamento_scaduto(self):
        dati_abbonamento = _crea_dati_abbonamento(durata=1)
        abbonamento = self._gestore_abbonamenti.crea_abbonamento(**dati_abbonamento)
        self.assertIsNotNone(abbonamento)

        atleta = Mock(spec=Atleta)
        self._gestore_atleti.get_atleta_per_id.return_value = atleta

        contratto1 = self._gestore_abbonamenti.crea_contratto(1, 1, datetime.date.fromisoformat("2025-07-01"))
        self.assertIsNotNone(contratto1)

        contratto2 = self._gestore_abbonamenti.crea_contratto(2, 1)
        self.assertIsNotNone(contratto2)

        controllo1 = self._gestore_abbonamenti.controllo_abbonamento_scaduto(1)
        controllo2 = self._gestore_abbonamenti.controllo_abbonamento_scaduto(2)
        self.assertEqual(controllo1, True)
        self.assertEqual(controllo2, False)