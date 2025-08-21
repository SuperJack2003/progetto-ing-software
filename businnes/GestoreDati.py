import pickle
from pathlib import Path

from domain.attività.atleta import Atleta
from domain.attività.allenatore import Allenatore

from domain.attività.contratto_atleta_corso import ContrattoAtletaCorso
from domain.attività.contratto_scheda import ContrattoScheda
from domain.attività.contratto_esercizio import ContrattoEsercizio
from domain.attività.contratto_abbonamento import ContrattoAbbonamento
from domain.attività.contratto_atleta_allenatore import ContrattoAtletaAllenatore
from domain.attività.contratto_allenatore_corso import ContrattoAllenatoreCorso

cartella_dati = Path(__file__).parent.parent / 'data'
cartella_dati.mkdir(parents=True, exist_ok=True)

def carica_dati():
    try:
        with open(cartella_dati / 'utenti.pkl', 'rb') as f:
            print ("Caricamento utenti...")

            lista_utenti = pickle.load(f)
            lista_atleti = []
            lista_allenatori = []

            for utente in lista_utenti:
                if isinstance(utente, Atleta):
                    lista_atleti.append(utente)

                elif isinstance(utente, Allenatore):
                    lista_allenatori.append(utente)

        with open(cartella_dati / 'abbonamenti.pkl', 'rb') as f:
            print ("Caricamento abbonamenti...")

            lista_abbonamenti = pickle.load(f)

        with open(cartella_dati / 'corsi.pkl', 'rb') as f:
            print ("Caricamento corsi...")

            lista_corsi = pickle.load(f)

        with open(cartella_dati / 'schede.pkl', 'rb') as f:
            print ("Caricamento schede...")

            lista_schede = pickle.load(f)

        with open(cartella_dati / 'esercizi.pkl', 'rb') as f:
            print ("Caricamento esercizi...")

            lista_esercizi = pickle.load(f)

        with open(cartella_dati / 'contratti.pkl', 'rb') as f:
            print("Caricamento contratti...")

            lista_contratti = pickle.load(f)
            lista_contratti_abbonamento = []
            lista_contratti_scheda = []
            lista_contratti_esercizio = []
            lista_contratti_allenatore_corso = []
            lista_contratti_atleta_corso = []
            lista_contratti_allenatore_atleta = []

            for contratto in lista_contratti:
                if isinstance(contratto, ContrattoAbbonamento):
                    lista_contratti_abbonamento.append(contratto)

                elif isinstance(contratto, ContrattoScheda):
                    lista_contratti_scheda.append(contratto)

                elif isinstance(contratto, ContrattoEsercizio):
                    lista_contratti_esercizio.append(contratto)

                elif isinstance(contratto, ContrattoAllenatoreCorso):
                    lista_contratti_allenatore_corso.append(contratto)

                elif isinstance(contratto, ContrattoAtletaCorso):
                    lista_contratti_atleta_corso.append(contratto)

                elif isinstance(contratto, ContrattoAtletaAllenatore):
                    lista_contratti_allenatore_atleta.append(contratto)

        with open(cartella_dati / 'notifiche.pkl', 'wb') as f:
            print ("Caricamento notifiche...")

            lista_notifiche = pickle.load(f)

    except FileNotFoundError:
        print(f"File {f}")