import random

print("1.Variabili Numeriche")
print("2.Stringhe")
print("3.Operatori Logigi ")
print("4.Liste")
print("5.Tuple")
print("6.Insieme")
print("7.Controllo del flusso")
print("8.Ciclo")
print("9.Range e *range()")
print("10.Funzioni")



scelta=int(input("Di cosa vogliamo parlare? "))

match scelta:
    case 1:
        print("Le variabili\n")
        print("Le variabili numeriche in Python sono utilizzate per memorizzare valori numerici.Questi valori possono essere interi, decimali o complessi.Ecco i principali tipi di variabili numeriche in Python:")
        print("\nint- Intero")
        a=24
        b=-5
        print(f"\nIl numero intero a è {a}")
        print(f"Il numero intero a è {b}")
        print("\nfloat-numeri con la virgola mobile")
        a=24.5
        b=-5.5
        print(f"\nIl numero intero a è {a}")
        print(f"Il numero intero a è {b}")
        print("\nVariabili Booleano: assumonbo 2 valori: True/False")
        x=True
        y=False
        print("\nIl corso è interessante? (True/False)",x)
    case 2:
        print("Stringhe\n")
        print("\nLa stringa è una sequenza di caratteri racchiusa tra virgolette singole (') o doppie (''). Le stringhe possono contenere testo, numeri, simboli e spazi. Ogni carattere di una stringa ha una posizione (indice), a partire da 0. Puoi accedere a ogni carattere tramite l'indice. ")
        parola="Liliana"
        
        lunghezza=len(parola)
        print(f"\n{parola}")
        print("La prima lettera risulta: ",parola[0])
        print(f"{parola} contiene {lunghezza} caratteri.")
    case 3:
        print("Operatori Logici\n")
        print("Gli operatori logici in Python vengono utilizzati per combinare espressioni booleane (veri/falsi) \ne restituire un risultato booleano. Sono fondamentali per le operazioni di condizionali\ne controllo del flusso del programma.")
        a = int(input("Inserisci un numero: "))
        b = int(input("Inserisci un numero: "))
        # Esempio con and
        if a > 0 and b > 0:
            print("Entrambi i numeri sono positivi.")
        # Esempio con or
        if a < 0 or b > 0:
            print("Almeno uno dei numeri è positivo.")
        # Esempio con not
        if not(a < 0):
            print(f"Il numero a={a} non è negativo.")
        # Operatore di uguaglianza (==)
        print(f"I numeri a={a} e b={b} sono uguali? Risultato: {a == b}")
        # Operatore di disuguaglianza (!=)
        print(f"I numeri a={a} e b={b} sono diversi? Risultato: {a != b}")
        # Operatore maggiore di (>)
        print(f"I numeri a={a} è maggiore di b={b}? Risultato: {a > b}")
        # Operatore minore di (<)
        print(f"I numeri a={a} è minore di b={b}? Risultato: {a < b}")
        # Operatore maggiore o uguale a (>=)
        print(f"I numeri a={a} è maggiore o uguale a b={b}? Risultato: {a >= b}")
        # Operatore minore o uguale a (<=)
        print(f"I numeri a={a} è minore o uguale a b={b}? Risultato: {a <= b}")
    case 4:
        print("\nListe\n")
        print("Una lista è una collezione ordinata e mutabile di elementi. Può contenere qualsiasi tipo di dato.")
        
        lista = [10, 20, 30, 40, 50, 70, 90]
        print("Lista: ", lista)
        print("Il primo elemento della lista è: ", lista[0])
        print("Il quarto elemento della lista è: ", lista[3])  
        
        # 1. append(): Aggiungi un elemento alla fine della lista
        lista.append(60)
        print(f"Lista dopo append(60): {lista}  -> Aggiungiamo il numero 60 alla fine della lista")

        # 2. insert(): Aggiungi un elemento in una posizione specifica
        lista.insert(2, 25)  # Inserisce 25 alla posizione 2
        print(f"Lista dopo insert(2, 25): {lista}  -> Aggiungiamo il numero 25 nella posizione 2")

        # 3. remove(): Rimuove il primo elemento che corrisponde al valore dato
        lista.remove(20)  # Rimuove il primo 20
        print(f"Lista dopo remove(20): {lista}  -> Rimuoviamo il numero 20 dalla lista")

        # 4. pop(): Rimuove e restituisce l'elemento alla posizione specificata 
        rimosso = lista.pop(3)  # Rimuove l'elemento alla posizione 3
        print(f"Lista dopo pop(3): {lista}  -> Rimuoviamo l'elemento alla posizione 3: {rimosso}")

        # 5. sort(): Ordina la lista in ordine crescente (modifica la lista stessa)
        lista.sort()
        print(f"Lista dopo sort(): {lista}  -> Ordiniamo la lista in ordine crescente")

        # 6. reverse(): Inverte l'ordine degli elementi nella lista
        lista.reverse()
        print(f"Lista dopo reverse(): {lista}  -> Invertiamo l'ordine della lista")

        # 7. count(): Conta quante volte un valore appare nella lista
        conta = lista.count(50)
        print(f"Numero di occorrenze di 50: {conta} -> Contiamo quante volte appare il numero 50 nella lista")
        # 8. len(): Restituisce il numero di elementi nella lista
        lunghezza = len(lista)
        print(f"Lunghezza della lista: {lunghezza} -> Mostriamo la lunghezza della lista")

    case 5:
        print("\nTuple")
        print("\nUna tuple è una collezione ordinata e immutabile di elementi. A differenza delle liste, una volta che una tuple è stata creata,i suoi elementi non possono essere modificati, aggiunti o rimossi.")
        tupla = (1, "ciao", 3, "banana")  # Tuple mista
        print("La Tupla è pari: ",tupla)
        sottotupla = tupla[1:3]
        print("La sottotupla è pari: ",sottotupla)
    
    case 6:
        print("Un insieme (o set) è una collezione di elementi unici e non ordinati. A differenza delle liste e delle tuple, gli insiemi non mantengono un ordine specifico per gli elementi, e non permettono duplicati.")
        # Creazione di un insieme con parentesi graffe
        insieme = {2,3,4,5,6,8}
        # Creazione di un insieme con la funzione set()
        insieme2 = set([2,3,4,5,6,8])
        # 1. add(): Aggiungere un elemento all'insieme
        insieme.add(6)
        print(f"Insieme dopo add(6): {insieme}  -> Aggiungiamo il numero 6 all'insieme")
        # 2. remove(): Rimuovere un elemento dall'insieme
        insieme.remove(4)
        print(f"Insieme dopo remove(4): {insieme}  -> Rimuoviamo il numero 4 dall'insieme")
        # 3. discard(): Rimuovere un elemento 
        insieme.discard(3)
        print(f"Insieme dopo discard(3): {insieme}  -> Rimuoviamo il numero 3 dall'insieme ")
        # 4. union(): Unione di due insiemi
        unione = insieme.union(insieme2)
        print(f"Insieme dopo union(insieme2): {unione}  -> Uniamo insieme e insieme2")
        # 5. intersection(): Intersezione di due insiemi
        intersezione = insieme.intersection(insieme2)
        print(f"Insieme dopo intersection(insieme2): {intersezione}  -> Intersezione tra insieme e insieme2")
        # 6. difference(): Differenza tra due insiemi
        differenza = insieme.difference(insieme2)
        print(f"Insieme dopo difference(insieme2): {differenza}  -> Gli elementi di insieme che non sono in insieme2")
        # 7. symmetric_difference(): Differenza simmetrica tra due insiemi
        differenza_simmetrica = insieme.symmetric_difference(insieme2)
        print(f"Insieme dopo symmetric_difference(insieme2): {differenza_simmetrica}  -> Differenza simmetrica tra insieme e insieme2")
        # 8. in: Verifica se un elemento è presente nell'insieme
        print(f"10 in insieme? {10 in insieme}  -> Verifica se 10 è presente nell'insieme")
        print(f"5 in insieme? {5 in insieme}  -> Verifica se 5 è presente nell'insieme")
        # 9. len(): Ottiene la lunghezza dell'insieme
        print(f"Lunghezza di insieme: {len(insieme)}  -> Mostriamo la lunghezza dell'insieme")
        # 10. clear(): Rimuove tutti gli elementi dall'insieme
        insieme.clear()
        print(f"Insieme dopo clear(): {insieme}  -> L'insieme è stato svuotato")
  
        # 11. intersection_update(): Intersezione dell'insieme corrente con un altro, modifica l'insieme originale
        insieme2.intersection_update(insieme)
        print(f"Insieme dopo intersection_update(insieme): {insieme2}  -> Modifichiamo insieme2 con l'intersezione con insieme")

        # 12. difference_update(): Differenza dell'insieme corrente con un altro, modifica l'insieme originale
        insieme2.difference_update(insieme)
        print(f"Insieme dopo difference_update(insieme): {insieme2}  -> Modifichiamo insieme2 con la differenza con insieme")

        # 13. isdisjoint(): Verifica se due insiemi non hanno elementi in comune
        disjoint_check = insieme.isdisjoint(insieme2)
        print(f"Insieme e insieme2 sono disgiunti? {disjoint_check}  -> Verifica se insieme e insieme2 non hanno elementi in comune")



    case 7:
        print("\n Controllo del flusso")
        print("Il controllo del flusso viene utilizzato per eseguire il codice solo se una certa condizione è vera. Le strutture di controllo condizionali sono if, elif, else e match.")
        lista=[*range(1,11)] #lista immutabile
        #liste vuote
        lista_pari=[] 
        lista_dispari=[]
        somma_num_pari=0
        somma_num_dispari=0
        #ciclo for per la creazione di una lista con numeri pari e una lista numeri dispari
        for num in lista:
            if num%2==0:
                lista_pari.append(num)
                somma_num_pari+= num
                
            else:
                lista_dispari.append(num)
                somma_num_dispari+=num
        print("I numeri pari risultano essere: ", lista_pari)
        print("I numeri dispari risultano essere: ", lista_dispari)
    
    case 8:
        print("\n Cicli")
        print("I cicli sono strutture di controllo che consentono di eseguire una porzione di codice più volte, finché una determinata condizione è vera. I due tipi di ciclo sono for e while.")
        
        ciclo=int(input("Ciclo for (1) o Ciclo while (2): "))
        if ciclo==1:
            for i in range(5):  
                print(i) #Stampa i numeri da 0 a 4
        else:
            i = 0
            while i < 5:
                print(i)  # Stampa i numeri da 0 a 4
                i += 1  
        print("\n Break viene utilizzata per uscire immediatamente da un ciclo, sia esso for o while, anche se la condizione del ciclo non è stata soddisfatta completamente.")
        for i in range(10):
            if i == 5:
                print("Interrompo il ciclo quando i è uguale a 5")
                break  # Esce dal ciclo quando i è 5
            print(i)
            
        print("\nContinue fa sì che il ciclo salti l'iterazione corrente e prosegua con la successiva.")
        for i in range(10):
            if i == 5:
                continue  # Salta il ciclo quando i è 5
            print(i)
        
        print("\npass non fa nulla e viene usato come un segnaposto, per indicare che un blocco di codice è vuoto. ")
        for i in range(10):
            if i == 5:
                pass  # Non fare nulla quando i è 5
            else:
                print(i)
                
                
    case 9:
        print("\nrange() è utilizzata per generare una sequenza di numeri.")
        print("range(start, stop, step)")
        print("1.start (opzionale): È il numero da cui iniziare. Se non fornito, il valore predefinito è 0.\n2.stop (obbligatorio): È il numero fino a cui la sequenza arriva, escluso.\n3.step (opzionale): È l'incremento tra ogni numero nella sequenza. Se non fornito, il valore predefinito è 1.")
        print("* (splat) viene usato per 'espandere' un oggetto iterabile (come una lista, un tuple o un range) in singoli valori. Non è modificabile")
        
        numeri= [*range(1, 6)]
        for numero in numeri:
            print(numero)
    
    case 10:
       print(" Una funzione è un blocco di codice che esegue un'operazione specifica e può essere riutilizzato in diverse parti del programma. Le funzioni aiutano a organizzare il codice in modo più leggibile, modulare e riutilizzabile.")
       print("def -> Parola chiave che viene utilizzata per dichiarare una funzione.")
       print("nome_funzione()-> Il nome che scegli per la funzione.")
       print("parametri->  I parametri sono variabili che possono essere utilizzate all'interno del corpo della funzione.")
       print("return-> Una funzione può restituire un valore tramite return")
       
       print("Proviamo insieme: ")
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

inserimento_dati()

# Stampa i dati inseriti
print("\nDati inseriti:")
for dato in dati:
    print(dato) 

        

            
            
        

        




        










""" 
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
    

            

            
        
    
        
                
            
     """