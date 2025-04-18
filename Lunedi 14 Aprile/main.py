from army_utilities import Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione
from army_controll import ControlloMilitare


def main():
    # Creazione delle unità militari
    fanteria1 = Fanteria("Alpha", 100, "Capitano", 90)
    artiglieria1 = Artiglieria("Bravo", 8, "Obice")
    cavalleria1 = Cavalleria("CavalloFiero", 40, "Leggera", 12, 75)
    supporto1 = SupportoLogistico("Delta", 20, {"munizioni": 150, "cibo": 100})
    ricognizione1 = Ricognizione("Echo", 10, 15, 85)

    # Registrazione unità grazie al Controllo Militare
    ControlloMilitare.registra_unità(fanteria1)
    ControlloMilitare.registra_unità(artiglieria1)
    ControlloMilitare.registra_unità(cavalleria1)
    ControlloMilitare.registra_unità(supporto1)
    ControlloMilitare.registra_unità(ricognizione1)

    print("\n--- Mostra tutte le unità registrate ---")
    ControlloMilitare.mostra_unità()
    # Esempio con i dettagli dell'unità 'Echo'
    print("\n--- Dettagli unità 'Echo' ---")
    ControlloMilitare.dettagli_unità("Echo")
    # Esempio di azioni specifiche eseguite dalle unità
    print("\n--- Azioni esempio ---")
    fanteria1.costruisci_trincea()
    artiglieria1.calibra_artiglieria()
    cavalleria1.esplora_terreno()
    supporto1.mostra_scorte()
    ricognizione1.conduci_ricognizione()
    ricognizione1.intercettato()

# Entry Point
if __name__ == "__main__":
    main()