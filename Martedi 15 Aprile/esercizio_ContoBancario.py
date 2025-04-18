

# classe conto bancario 

class ContoBancario():
    clienti_banca={
    'Alice': 246.19,
    'Marco': 450.03,
    'Giulia': 3727.56,
    'Luca': 4866.76,
    'Sara': 1018.95,
    'Davide': 768.51,
    'Elena': 3361.72,
    'Francesco': 4291.73,
    'Chiara': 717.03,
    'Giorgio': 660.72
}
    def __init__(self):
        self.__titolare=input("Inserisci il tuo nome")
        self.__saldo=self.clienti_banca[self.__titolare]
    
    def get_saldo(self): 
        return self.__saldo
    

    def set_deposita(self): #modificare
        importo=float(input("Inserire importo da depositare: "))
        if importo > 0:
            self.__saldo += importo
            print(f"Hai depositato {importo}€. Nuovo saldo: {self.__saldo}€.")
        else:
            print("Nessun importo da depositare")
            
    def set_preleva(self):
        importo = float(input("Inserire importo da prelevare: "))
        if importo > 0 and self.__saldo >= importo:
            self.__saldo -= importo
            print(f"Hai prelevato {importo}€. Nuovo saldo: {self.__saldo}€.")
        else:
            print("Importo non valido o saldo insufficiente.")
                
    def visulizza_saldo(self):
        nome=input("Inserisci il nome:")
        if nome in self.clienti_banca:
           print(f"Il cliente {nome} ha il seguente saldo {self.__saldo}€") 
        else:
            print("Cliente non trovato")   
    

conto = ContoBancario()

while True:
    print("\n--- MENU OPERAZIONI BANCA ---")
    print("1. Visualizza saldo")
    print("2. Deposita")
    print("3. Preleva")
    print("4. Esci")

    scelta = input("Scegli un'opzione (1-4): ")

    match scelta:
        case "1":
            print(f"Saldo attuale: {conto.get_saldo()}€")
        case "2":
            conto.set_deposita()
        case "3":
            conto.set_preleva()
        case "4":
            print("Grazie per aver utilizzato il servizio bancario. Arrivederci!")
        case _:
            print("Scelta non valida. Riprova.")

        

        