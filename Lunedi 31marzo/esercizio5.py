""" esercizio 4: Scrivi un sistema che prende in input una lista di numeri interi che 
precedentemente è stata valorizzata dall’utente. 
Il sistema deve:

1. Utilizzare un ciclo for per trovare il numero massimo nella lista.

2. Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.

3. Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota, 
altrimenti stampare il numero massimo trovato e il numero di elementi nella lista. """

element=int(input("inserisci un numero: "))
conteggio=0
lista=[]
# inserisco da tastiera ciascun elemento 
while conteggio<element:
    num=int(input("inserisci numero: "))
    lista.append(num)
    conteggio +=1 
    
print("il numero di elemnti nella lista sono ", conteggio)

# lista è vuota se la lunghezza risulta essere 0 
# altrimenti -> stampare il massimo 
if len(lista)==0:
    print("Lista vuota")
else: 
    for i in lista:
        if i>=max(lista):
            massimo=i
            print("Il numero massimo all'interno della lista è",massimo)
            
            
""" element=int(input("inserisci un numero: "))
conteggio=0
lista=[]
# inserisco da tastiera ciascun elemento 
while conteggio<element:
    num=int(input("inserisci numero: "))
    lista.append(num)
    conteggio +=1 
    if len(lista)==0:
        print("Lista vuota")
    else: 
        for i in lista:
            if i>=max(lista):
                massimo=i

print("Il numero massimo all'interno della lista è",massimo)
print("il numero di elemnti nella lista sono ", conteggio) """
    

   
        
        
    
    
        