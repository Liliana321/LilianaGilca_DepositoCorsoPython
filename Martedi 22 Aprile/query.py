import csv
import mysql.connector

from Analisi_statistiche import analisi_st

#from Analisi_statistiche import analisi_st

# Parametri di connessione
host = "localhost"
user = "root"
password = "root"
port = 8889
database = "Centro_estetico"

# Connessione al database ora esistente
myDB = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    port=port,
    database=database
)
cursor = myDB.cursor()

def somma_totale_vendite():
    query = '''
    SELECT 
        prodotti.nome_prodotto,
        SUM(vendite.quantità_acquistate) AS tot_quantità
    FROM 
        vendite
    JOIN 
        prodotti ON vendite.id_prodotto = prodotti.id_prodotto
    GROUP BY 
        prodotti.nome_prodotto
        '''
    cursor.execute(query)
    quantita = [int(row[1]) for row in cursor.fetchall()]
    print(f"\n👉 Somma totale delle vendite registrate: {sum(quantita)}")

def media_acquisti_per_prodotto():
    query = '''
    SELECT 
        id_prodotto, 
        SUM(quantità_acquistate) AS totale
    FROM 
        vendite
    GROUP BY 
        id_prodotto
    '''
    cursor.execute(query)
    totali = [int(row[1]) for row in cursor.fetchall()]
    analisi = analisi_st(totali)
    print(f"\n📊 Media acquisti per prodotto: {analisi.mean():.2f}")

# Menu
while True:
    print("\n--- MENU ANALISI ---")
    print("1. Somma vendite registrate")
    print("2. Media acquisti per prodotto")
    print("0. Esci")

    scelta = input("Scegli un'opzione: ")

    if scelta == "1":
        somma_totale_vendite()
    elif scelta == "2":
        media_acquisti_per_prodotto()
    elif scelta == "0":
        print("👋 Uscita dal programma.")
        break
    else:
        print("❌ Scelta non valida. Riprova.")

# Chiusura DB
cursor.close()
myDB.close()

