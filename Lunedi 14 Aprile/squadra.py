# Classe base per rappresentare un membro della squadra. classe padre 
class MembroSquadra():
    #costruttore
    def __init__(self,nome,eta):
        self.nome = nome  # Inizializza il nome
        self.eta = eta    # Inizializza l'età
        
    def descrivi(self):
        print(f"{self.nome} ha {self.eta} e fa parte della squadra!")  # Descrizione base del membro

# Sottoclasse che rappresenta un giocatore, eredita da MembroSquadra
class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        self.ruolo = ruolo               # Inizializza il ruolo del giocatore
        self.numero_maglia = numero_maglia  # Inizializza il numero di maglia
        super().__init__(nome, eta)     # Chiama il costruttore della classe base
        
    def gioca_partita(self):
        print(f"Il giocatore {self.nome} gioca come {self.ruolo} nella partita con la maglia numero {self.numero_maglia}")

# Sottoclasse che rappresenta un allenatore
class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_esperienza):
        self.anni_esperienza = anni_esperienza  # Inizializza gli anni di esperienza
        super().__init__(nome, eta)                
        
    def dirige_allenamento(self):
        print(f"L'allenatore {self.nome} allena la squadra")  # Metodo per dirigere l'allenamento

# Sottoclasse che rappresenta un assistente
class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)              
        self.specializzazione = specializzazione # Inizializza la specializzazione
        
    def supporta_team(self):
        print(f"L'assistente {self.nome} supporta la squadra ricoprendo la seguente figura {self.specializzazione}")

    
def menu_squadra():
    membri = []  # Lista per salvare i membri creati

    while True:
        print("\n--- MENU SQUADRA ---")
        print("1. Aggiungi Giocatore")
        print("2. Aggiungi Allenatore")
        print("3. Aggiungi Assistente")
        print("4. Mostra Tutti i Membri")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione (1-5): ")

        if scelta == "1":
            nome = input("Nome del giocatore: ")
            eta = int(input("Età: "))
            ruolo = input("Ruolo: ")
            numero_maglia = int(input("Numero di maglia: "))
            g = Giocatore(nome, eta, ruolo, numero_maglia)
            membri.append(g)
            print("Giocatore aggiunto.")

        elif scelta == "2":
            nome = input("Nome dell'allenatore: ")
            eta = int(input("Età: "))
            anni = int(input("Anni di esperienza: "))
            a = Allenatore(nome, eta, anni)
            membri.append(a)
            print("Allenatore aggiunto.")

        elif scelta == "3":
            nome = input("Nome dell'assistente: ")
            eta = int(input("Età: "))
            spec = input("Specializzazione: ")
            ass = Assistente(nome, eta, spec)
            membri.append(ass)
            print("Assistente aggiunto.")

        elif scelta == "4":
            if not membri:
                print("Nessun membro nella squadra.")
            else:
                for m in membri:
                    m.descrivi()
                    if isinstance(m, Giocatore):
                        m.gioca_partita()
                    elif isinstance(m, Allenatore):
                        m.dirige_allenamento()
                    elif isinstance(m, Assistente):
                        m.supporta_team()

        elif scelta == "5":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")
     
menu_squadra()