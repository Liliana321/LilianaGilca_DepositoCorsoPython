# Esercizio Venerdi 4 Aprile 
# Inventario con i costi di produzione
inventario = {
    "Viti": 0.10,
    "Bulloni": 0.25,
    "Chiodi": 0.05,
    "Motori": 150.00,
    "Compressori": 300.00,
    "Cavi elettrici": 1.50,
    "Saldatori": 75.00,
    "Lampade industriali": 20.00,
    "Pneumatici": 45.00,
    "Rulli": 10.00
}

# Magazzino con le quantità dei prodotti
magazzino = {
    "Viti": 1200,
    "Bulloni": 800,
    "Chiodi": 1500,
    "Motori": 250,
    "Compressori": 50,
    "Cavi elettrici": 500,
    "Saldatori": 30,
    "Lampade industriali": 100,
    "Pneumatici": 200,
    "Rulli": 300
}

# Prezzi di vendita dei prodotti
vendita_prezzo = {
    "Viti": 0.20,
    "Bulloni": 0.50,
    "Chiodi": 0.15,
    "Motori": 350.00,
    "Compressori": 600.00,
    "Cavi elettrici": 4.50,
    "Saldatori": 180.00,
    "Lampade industriali": 40.00,
    "Pneumatici": 90.00,
    "Rulli": 20.00
}
# classe prodotto che ha come attributo nome,
class Prodotto:
    #costruttore
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        
        self.nome = nome
        self.costo_produzione=costo_produzione
        self.prezzo_vendita=prezzo_vendita

        
class Fabbrica:
    def __init__(self,inventario):
        self.magazzino = magazzino
        self.inventario=inventario
        self.vendita_prezzo=vendita_prezzo 


    def aggiungi_prodotto(self):
        prodotto= input("Inserisci il nome del prodotto")
        quantità=int(input("inserisci quantità prodotto"))
        prezzo=float(input("inserisci prezzo prodotto"))
        if prodotto in self.magazzino:
            self.magazzino[prodotto]+=quantità
            self.vendita_prezzo[prodotto]+=prezzo
            print(f"Aggiornamento {prodotto}:{self.magazzino[prodotto]}")
            print(f"Aggiornamento {prodotto}:{self.vendita_prezzo[prodotto]}")
        else:
            self.magazzino[prodotto]=quantità
            self.vendita_prezzo[prodotto]+=prezzo
            print(f"Aggiunto {prodotto}:{quantità}")
    
    def vendita_prodotto(self):
        prodotto=input("Tra i vari prodotti scegli quello da vendere: ")
        quantità_venduta=int(input("Inserisci la quantità da vendere: "))
        self.magazzino[prodotto]-=quantità_venduta
        prezzo_prodotto = vendita_prezzo[prodotto]
        profitto=quantità_venduta*prezzo_prodotto
        print(f" Il prodotto {prodotto} è stato venduto a {prezzo_prodotto} per un totale di {quantità_venduta} unità.\n Il Profitto è pari a {profitto}")
    
    def resi_prodotto(self):
        prodotto=input("Nome prodotto per il reso: ")
        quantità_reso=int(input("Inserisci la quantità da rendere: "))
        self.magazzino[prodotto]+=quantità_reso

fabbrica = Fabbrica(inventario)


print("Aggiungere un prodotto (1)")
print("Vendere un prodotto (2)")
print("Effettuare Resi (3)")

while True:
    scelta=int(input("Scegliere l'operazione da effettuare"))
    if scelta=="":
        break
    if scelta==1:
        fabbrica.aggiungi_prodotto()
    elif scelta==2:
        fabbrica.vendita_prodotto_prodotto()
    else:
        fabbrica.resi_prodotto()
        
#Cacciaviti