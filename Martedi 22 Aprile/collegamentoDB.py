'''
Esercizio per la creazione del database per ripasso numpy 

in questo file strutturo il collegamento 

'''

import csv
import mysql.connector

# Parametri di connessione
host = "localhost"
user = "root"
password = "root"
port = 8889
database = "Centro_estetico"


# Connessione al database
connessione = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    port=port
)
cursor = connessione.cursor()

# Creazione del database se non esiste
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
print(f"Database '{database}' verificato o creato.")
cursor.close()
conn.close()

# Connessione al database ora esistente
myDB = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    port=port,
    database=database
)
cursor = myDB.cursor()

# Funzione per importare un CSV in una tabella
def importa_csv(nome_file, nome_tabella):
    with open(nome_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader) 
        rows = list(reader)   

    # Creazione tabella
    columns = ", ".join(f"{col} TEXT" for col in header)
    create_stmt = f"CREATE TABLE IF NOT EXISTS {nome_tabella} ({columns});"
    cursor.execute(create_stmt)

    # Inserimento righe
    cols = ", ".join(header)
    placeholders = ", ".join(["%s"] * len(header))
    insert_stmt = f"INSERT INTO {nome_tabella} ({cols}) VALUES ({placeholders})"
    for row in rows:
        cursor.execute(insert_stmt, row)

    myDB.commit()
    print(f"{len(rows)} righe inserite nella tabella {nome_tabella}.")

# Importazione dei tre file
importa_csv("clienti_femmine.csv", "clienti")
importa_csv("prodotti_estetica_aggiornato.csv", "prodotti")
importa_csv("vendite_estetica_aggiornato.csv", "vendite")

# Chiusura della connessione
#cursor.close()
#myDB.close()
