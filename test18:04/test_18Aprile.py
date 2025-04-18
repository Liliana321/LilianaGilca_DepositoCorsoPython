'''
Implementa in Python un piccolo sistema di gestione di veicoli 
che dimostri incapsulamento, ereditarietà e polimorfismo.
'''

'''
Definire una classe base Veicolo con attributi protetti(Marca[Str], Anno di immatricolazione[Int], 
Targa [Str] e Revisione[Bool]  ) e metodi getter/setter. 
'''

class Veicolo():
    
    def __init__(self,marca,anno_immatricolazione,targa,revisione):
        
        self._marca=marca
        self._anno_immatricolazione=anno_immatricolazione
        self._targa=targa
        self._revisione=revisione
    # getter e setter per marca   
    def get_marca(self):
        return self._marca

    def set_marca(self, nuova_marca):
        self._marca = nuova_marca
    # getter e setter per anno    
    def get_anno_immatricolazione(self):
        return self._anno_immatricolazione

    def set_anno(self, nuova_anno_immatricolazione):
        self._anno_immatricolazione = nuova_anno_immatricolazione
    # getter e setter per targa   
    def get_targa(self):
        return self._targa

    def set_targa(self, nuova_targa):
        self._targa = nuova_targa
    # getter e setter per revisione   
    def get_revisione(self):
        return self._revisione

    def set_revisione(self, nuova_revisione):
        self._revisione = nuova_revisione
   
    # funzione per descrizione dell'automobile
    def descrivi(self):
        return f"Marca: {self._marca}, Anno: {self._anno_immatricolazione}, Targa: {self._targa}, Revisione: {self._revisione}" 
   
'''
Creare tre sottoclassi (Auto, Moto, Camion) che ereditano da Veicolo e sovrascrivono un metodo comune 
(descrivi())che riporti tutti i dati dell'oggetto reale, ogni classe figlia deve avere un attributo unico .
'''

     
class Auto(Veicolo):
    def __init__(self,tipologia,marca,anno_immatricolazione,targa,revisione):
        self.tipologia=tipologia # "SUV", "Berlina", "Utilitaria"
        super().__init__(marca,anno_immatricolazione,targa,revisione)
        
    def descrivi(self):
        return super().descrivi() + f", Tipologia: {self.tipologia}"
        
class Moto(Veicolo):
    def __init__(self,bauletto,marca,anno_immatricolazione,targa,revisione):
        self.bauletto=bauletto # boolean true:si false:no
        super().__init__(marca,anno_immatricolazione,targa,revisione)
        
    
    def descrivi(self):
        return super().descrivi() + f", bauletto: {self.bauletto}"
        
class Camion(Veicolo):
    def __init__(self,rimorchio,marca,anno_immatricolazione,targa,revisione):
        self.rimorchio=rimorchio# boolean true:si false:no
        super().__init__(marca,anno_immatricolazione,targa,revisione)
        
    
    def descrivi(self):
        return super().descrivi() + f", rimorchio: {self.rimorchio}"
    

def menu():
    veicoli={}
    id_veicoli=0
    
    while True:
        print("1. Crea Auto")
        print("2. Crea Moto")
        print("3. Crea Camion")
        print("4. Mostra tutti i veicoli (descrivi)")
        print("5. Esci")
        
        scelta = int(input("Scegli un'opzione: "))
        
        match scelta:
            case 1:
                #creazione auto
                tipologia = input("Inserisci la tipologia (SUV, Berlina, Utilitaria): ")
                marca = input("Inserisci la marca: ")
                anno = int(input("Inserisci l'anno di immatricolazione: "))
                targa = input("Inserisci la targa: ")
                revisione = bool(input("La revisione è valida? (True/False): "))
                auto = Auto(tipologia, marca, int(anno), targa, revisione)
                veicoli[id_veicoli]=auto
                auto.descrivi()
                id_veicoli +=1
                
            case 2:
                #moto
                bauletto = bool(input("La moto ha il bauletto? (True/False): "))
                marca = input("Inserisci la marca: ")
                anno = int(input("Inserisci l'anno di immatricolazione: "))
                targa = input("Inserisci la targa: ")
                revisione = bool(input("La revisione è valida? (True/False): "))
                moto = Moto(bauletto, marca, int(anno), targa, revisione)
                veicoli[id_veicoli]=moto
                moto.descrivi()
                id_veicoli +=1
                
            case 3:
                #camion
                rimorchio = bool(input("La moto ha il bauletto? (True/False): "))
                marca = input("Inserisci la marca: ")
                anno = int(input("Inserisci l'anno di immatricolazione: "))
                targa = input("Inserisci la targa: ")
                revisione = bool(input("La revisione è valida? (True/False): "))
                camion = Camion(rimorchio, marca, int(anno), targa, revisione)
                veicoli[id_veicoli]=camion
                camion.descrivi()
                id_veicoli +=1
                
            case 4:
                for id_vei,veicolo in veicoli.items():
                    print(f"ID {id_vei} → {veicolo.descrivi()}")
                    
            case _:
                print("Uscita dal programma")
                break
   
menu()                 
                