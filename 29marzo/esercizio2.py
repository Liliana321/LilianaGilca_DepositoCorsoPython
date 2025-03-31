'''Descrizione: Scrivi un programma che chiede all'utente di inserire
due numeri e un'operazione da eseguire tra addizione (+), sottrazione (-),
moltiplicazione (*) e divisione (/). Il programma dovrebbe poi eseguire 
l'operazione e stampare il risultato. Tuttavia, se l'utente tenta di 
dividere per zero, il programma dovrebbe stampare "Errore: Divisione 
per zero". Se l'operazione inserita non è riconosciuta, 
dovrebbe stampare "Operazione non valida". '''

# inserimento 2 numeri da parte dell'utenete 
num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

# inserimento operazione 
operazione=input("che operazione vuoi effettuare (a/s/m/d): ")

# condizioni per le operazioni, nel caso in cui si opta per una divisione per zero 
#il programma fornisce errore
match operazione:
    case "a":
        risultato = num1 + num2
        print(f"risultato addizione: {risultato}")
    case "s":
        risultato = num1 - num2
        print(f"risultato sottrazione: {risultato}")
    case "m":
        risultato = num1*num2
        print(f"Risultato moltiplicazione: {risultato}")
    case "d":
        if num2 == 0:
            print("Errore: Divisione per zero")
        else:
            risultato = num1 / num2
            print(f"risultato divisione: {risultato}")
    case _:
        print("Operazione non valida")