dati = []

def inserimento_dati():
    while True:
        name = input("Inserisci nome: ")
        numero = int(input("Inserisci numero: "))
        materia = input("Inserisci materia: ")
        credito = int(input("Inserisci credito: "))
        dati.append({'name': name, 'numero': numero, 'materia': materia, 'credito': credito})
        
        scelta = input("Vuoi inserire altri dati? (s/n): ")
        
        # Gestione della scelta dell'utente
        if scelta == "no":
            break  # Esce dal ciclo 
        elif scelta == "si":
            continue  # Continua il ciclo 
        else:
            print("Scelta non valida, si prega di riprovare.")

# Chiamata della funzione
inserimento_dati()

# Stampa i dati inseriti
print("\nDati inseriti:")
for dato in dati:
    print(dato)
print(dati)

# Funzione per calcolare la media ponderata
def statistiche(dati):
    if len(dati) == 0:
        print("Niente Statistiche")
        return
    
    somma_pesata = 0  # Somma dei numeri ponderati
    somma_crediti = 0  # Somma dei crediti
    
    for dato in dati:
        somma_pesata += dato['numero'] * dato['credito']  # Moltiplica il numero per il credito
        somma_crediti += dato['credito']  # Somma i crediti
    
    
    # Calcola la media ponderata
    media_ponderata = somma_pesata / somma_crediti
    print("\nStatistiche:")
    print(f"Media ponderata complessiva: {media_ponderata:.2f}")

# Chiamata della funzione per calcolare la media ponderata
statistiche(dati)

        
        
        
    