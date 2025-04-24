
import numpy as np


def menu():
    n=int(input("inserisci il numero di righe:"))
    m=int(input("Inserisci il numero di colonne:"))
    a=int(input("Inserisci estremo sx: "))
    b=int(input("Inserisci estremo dx:"))
    matrice=np.random.randint(a,b,size=(n,m)) 
    print(matrice)
    print("SCEGLI TRA QUESTE OPZIONI")
    print("1. Start")
    print("2. shape ")
    scelta=int(input("Inserisci operazione da effettuare:"))
    if scelta==1:
        opzione=input("Vuoi aggiungere altro? (righe-colonne)")
        if opzione=="righe":
            c=int(input("quante righe vuoi aggiungere"))
            arr=np.random.randint(a,b,size=(c,m))
            matrice_completa=np.vstack((matrice,arr)) # verticale 
            print(matrice_completa)
        elif opzione=="colonne":
            c=int(input("quante colonne vuoi aggiungere"))
            arr=np.random.randint(a,b,size=(n,c))
            matrice_completa=np.concatenate((matrice,arr)) #orizzonatale
            print(matrice_completa)
        else:
            print("Errore")
    elif scelta==2:
        print("Shape della matrice:", matrice.shape)
        
    else:
        print("Errore")

menu()


                    
            
            