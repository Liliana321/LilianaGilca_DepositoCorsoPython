""" Scrivi un programma che chiede all'utente la sua età. 
Se l'età è inferiore a 18 anni, il programma dovrebbe stampare 
"Mi dispiace, non puoi vedere questo film". Altrimenti, dovrebbe 
stampare "Puoi vedere questo film".
"""



# inserimento età da tastiera
età=int(input("inserisci la tua età: "))
if età <18:
    print("Mi dispiace,non puoi vedere questo film")
else:
    print("Puoi vedere questo film")
    
