#Esercizio 
#variabili 
name="Liliana" #stringa
età=24 #int
print(f"ciao, sono {name} e ho {età} anni")

#ciclo for per contare le lettere specifiche in una stringa 
conta = 0
 
for lettera in name:
    if lettera == "i":
        conta += 1

print(f"La lettera 'i' appare {conta} volte nel nome.") 

#LISTA E OPERAZIONI 
#creazione lista a partire dallo split *, uso del ciclo for e di if per iterare sui numeri della sequenza 
#e stampare lista dispari/pari e somma pari/dispari
lista=[*range(conta,età+1)]
lista_pari=[]
lista_dispari=[]
somma_num_pari=0
somma_num_dispari=0
for num in lista:
    if num%2==0:
        lista_pari.append(num)
        somma_num_pari+= num
        
    else:
        lista_dispari.append(num)
        somma_num_dispari+=num
        
print("Lista numeri pari:",lista_pari)
print("Lista  numeri dispari:",lista_dispari)

print(f"Lista numeri pari: {somma_num_pari}")
print(f"Lista numeri dispari: {somma_num_dispari}")

#ciclo while e uso di set 

import random
a=int(input("inserire un numero:"))
b=int(input(f"inserire un numero maggiore di {a} :"))

num_liste=5
conteggio=0

liste=set()

while conteggio < num_liste:
    lista = random.sample(range(a, b), 5)  # Crea una lista con 5 numeri casuali nell'intervallo [a, b]
    liste.update(lista)
    print("Lista:", lista)
    conteggio+= 1

print("Insieme totale di numeri unici:", liste)      
        
#Funzione 
dati=[]
def inserimento_dati():
    while True:
        name=input("inserisci nome: ")
        età=int(input("inserisci età: "))
        dati.append({'name':name,'età':età})
        scelta=input("vuoi inserire altri? (s/n): ")
        # Gestione della scelta dell'utente
        if scelta == "no":
            break  # Esce dal ciclo 
        elif scelta == "si":
            continue  # Continua il ciclo 
        else:
            print("scelta non valida, si prega di riprova.")

# Chiamata della funzione
inserimento_dati()

# Stampa i dati inseriti
print("\nDati inseriti:")
for dato in dati:
    print(dato)
    

            

            
        
    
        
                
            
    