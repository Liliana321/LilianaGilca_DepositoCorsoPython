""" Vai a creare un menu con match che ti permetta di 
muoverti fra le operazioni, e che permetta anche 
di creare multiple scelte, tipo, add e divisione ecc """

# inserimento 2 numeri da parte dell'utenete 
num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

# inserimento operazione 
operazione=input("che operazione vuoi effettuare (a/s/m/d): ")

altro=input("vuoi fare altre operazioni (si/no): ")
if altro==si:
    match operazione:
        case "a" and "s":
            risultato_a = num1 + num2
            risultato = num1 - num2
            print(f"risultato sottrazione: {risultato}")
            print(f"risultato addizione: {risultato}")
        case "a" and "m":
            risultato = num1 + num2
            risultato = num1 - num2
            print(f"risultato sottrazione: {risultato}")
            print(f"risultato addizione: {risultato}")
        