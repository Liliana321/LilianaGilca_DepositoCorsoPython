# dati login giusti 

corretto_name="Liliana"
corretto_pin=1234

# login
name=input("inserisci nome:")
pin=int(input("inserisci pin:"))

# condizione di controllo 

if name==corretto_name and pin==corretto_pin:
    print("Ciao ", name, "benvenuto")
     # scelta per l'utente 
    colore_preferito = input("Qual è il tuo colore preferito? ")
    animale_preferito= input("Qual è il tuo animale preferito? ")
    scelta = input("\nVuoi cambiare qualcosa? (colore/animale): ").lower()
    match scelta:
        case 'colore':
        # cambio colore 
            nuovo_colore = input("Inserisci il nuovo colore preferito: ")
            print("Hai cambiato il colore preferito in {nuovo_colore}.")
        case 'animale':
            nuovo_animale = input("Inserisci il nuovo animale preferito: ")
            print("Hai cambiato il colore preferito in {nuovo_animale}.")
        case _:
            print("Scelta non valida.")
else:
    print(" credenziali sono errate ")


