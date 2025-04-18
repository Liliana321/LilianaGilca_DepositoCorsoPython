
import random
import army_unit as unit

# cinque classi specializzate che ereditano dalla classe padre. Ogni classe estende la funzionalità di base con
# comportamenti unici,

# FANTERIA: rappresenta i soldati di terra. Può costruire una trincea se i punti salute dell’unità sono sufficienti. 
# L’azione è condizionata allo stato di salute dell’unità


class Fanteria(unit.UnitaMilitare):  # eredita da UnitaMilitare
    def __init__(self, nome, numero_soldati, grado_militare, punti_salute):
        super().__init__(nome, numero_soldati)
        self.grado_militare = grado_militare 
        self.punti_salute = punti_salute
        self.trincea_costruita = False
        
    def costruisci_trincea(self):
        if self.punti_salute > 80:
            self.trincea_costruita = True
            print(f"{self.nome} ha costruito una trincea.")
        else:
            print(f"{self.nome} non è in grado di costruire una trincea.") 

# ARTIGLIERIA: Include una funzione per calibrare l’artiglieria, 
# che può fallire se non ci sono abbastanza soldati per operarla, 

class Artiglieria(unit.UnitaMilitare):  # eredita da UnitaMilitare
    def __init__(self, nome, numero_soldati, tipo_artiglieria):
        super().__init__(nome, numero_soldati)
        self.tipo_artiglieria = tipo_artiglieria
    
    def calibra_artiglieria(self):
        if self.numero_soldati <= 5:
            print(f"{self.nome}: non ci sono abbastanza soldati per calibrare l'artiglieria.")
        else:
            print(f"{self.nome} calibrata")

# CAVALLERIA: Ha la capacità di esplorare il territorio, ma solo se la resistenza (che simula stanchezza di uomini e cavalli) è abbastanza alta. 
# La visibilità rappresenta il raggio d’azione.L’azione è condizionata dal livello stanchezza cavallo e cavalieri


class Cavalleria(unit.UnitaMilitare):  # eredita da UnitaMilitare
    def __init__(self, nome, numero_soldati, tipo_cavalleria,visibilita,resistenza):
        super().__init__(nome, numero_soldati)
        self.tipo_cavalleria = tipo_cavalleria
        self.visibilita=visibilita # raggio di esplorazione (int) KM
        self.resistenza=resistenza # livello stanchezza cavallo e cavalieri
        
    def esplora_terreno(self):
        if self.resistenza<20:
            print(f"{self.nome} è troppo stanca per esplorare il terreno.")
        else:
            print(f"{self.nome} ha esplorato un'area di {self.visibilita} km ")
 
# SUPPORTOLOGISTICO: questa classe si occupa della gestione dei rifornimenti 
# Include anche una funzione per mostrare lo stato attuale delle scorte.

           
class SupportoLogistico(unit.UnitaMilitare):
    def __init__(self, nome, numero_soldati, scorte_iniziali):
        super().__init__(nome, numero_soldati)
        self.scorte = scorte_iniziali  # Dizionario: {'munizioni': 100, 'cibo': 50, ...}
    
    def rifornisci(self, altra_unità, tipo, quantità):
        if tipo in self.scorte and self.scorte[tipo] >= quantità:
            self.scorte[tipo] -= quantità
            print(f"{self.nome} ha rifornito {altra_unità.nome} con {quantità} unità di {tipo}.")
        else:
            print(f"{self.nome} non ha abbastanza {tipo} per rifornire {altra_unità.nome}.")

    def mostra_scorte(self):
        print(f"Scorte attuali di {self.nome}:")
        for k, v in self.scorte.items():
            print(f" - {k}: {v}")

# RICOGNIZIONE: Può esplorare aree senza farsi notare, con probabilità di essere intercettata,
# calcolata casualmente in base alla “silenziosità” dell’unità. 

class Ricognizione(unit.UnitaMilitare):
    def __init__(self, nome, numero_soldati, visibilità, silenziosità):
        super().__init__(nome, numero_soldati)
        self.visibilità = visibilità  # raggio di esplorazione in km
        self.silenziosità = silenziosità  # da 0 a 100: più alto, meno rilevabile

    def conduci_ricognizione(self):
        print(f"{self.nome} ha esplorato {self.visibilità} km di territorio senza essere rilevata.")
    
    def intercettato(self):
        rischio = random.randint(0, 100)
        if rischio > self.silenziosità:
            print(f"{self.nome} è stata intercettata durante la missione!")
            return True
        else:
            print(f"{self.nome} è rientrata senza essere rilevata.")
            return False