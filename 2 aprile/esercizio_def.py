# Esercizio 1
""" Crea una funzione chiamata quadrato(numero) 
che riceve un numero come parametro e restituisce il suo quadrato. """

# funzione che prende un unico parametro 

def quadrato(numero):
    quadrato=numero*numero
    print("Il quadrato risulta essere:", quadrato)

quadrato(2)
quadrato(4)


# Esercizio 2 
""" Crea una funzione chiamata somma_lista(lista) che riceve una lista 
di numeri e restituisce la somma di tutti gli elementi della lista. """


#random.sample(population:L’insieme (lista, range, stringa, ecc.) 
# da cui estrarre gli elementi, k)
import random

# funzione per la somma degli elementi della lista 
def somma_lista():
    # input estremi lista
    a=int(input("inserisci estremo inf:"))
    b=int(input("inserisci estremo sup:"))

    # randomizzazione lista 
    lista = random.sample(range(a, b), 5) 
    print("Lista:",lista)
    somma=sum(lista)
    
    #opzione per l'aggiunta liste random
    scelta=input("Vuoi aggiungere altre liste?(s/n):")
    match scelta:
        case "si":
            #input il numero delle liste 
            n = int(input("Quante liste vuoi in totale (considerando la prima)? "))
            somma_totale = somma  # partiamo già con la somma della prima lista

            for i in range(2, n + 1):  # da lista 2 fino a n. NB range(1,5)=1,2,3,4
                lista_aggiunta = random.sample(range(a, b), 5)
                somma_lista_aggiunta= sum(lista_aggiunta)
                somma_totale += somma_lista_aggiunta
                print(f"Lista {i}:",lista_aggiunta)
                print(f"Somma lista {i}:", somma_lista_aggiunta)
                

            print("Somma totale di tutte le liste:", somma_totale)

        case "no":
            print("Lista:",lista)
            print("Somma della prima lista: ",somma) 
            
    
somma_lista()