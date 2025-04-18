
'''
Realizza un’app console Python con menu che si connetta a un database MySQL 
per gestire una rubrica contatti.

'''

import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=8889,
    database="rubrica" 
)

print(myDB)

myCursor = myDB.cursor()

#Creazione del database
#query="CREATE DATABASE IF NOT EXISTS rubrica"
#myCursor.execute(query)

#creazione tabella contatti 
query = """
CREATE TABLE IF NOT EXISTS contatti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    email VARCHAR(50)
)
"""
myCursor.execute(query)
query = """
CREATE TABLE IF NOT EXISTS utenti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""
myCursor.execute(query)


def inserisci_contatto(utente_id):
    nome = input("Nome: ")
    telefono = int(input("Telefono: "))
    email = input("Email: ")

    query = "INSERT INTO contatti (nome, telefono, email) VALUES (%s, %s, %s)"
    myCursor.execute(query, (nome, telefono, email))

    print(" Contatto inserito con successo.")

def visualizza_contatti(utente_id):
    query="SELECT * FROM contatti"
    myCursor.execute(query)
    risultati = myCursor.fetchall()

    if risultati:
        for riga in risultati:
            print(f"ID: {riga[0]}, Nome: {riga[1]}, Telefono: {riga[2]}, Email: {riga[3]}")
    else:
        print(" Nessun elemento trovato.")
        
class Utente:
    def __init__(self, nome, password):
        self.nome = nome
        self.password = password

    def registra(self):
        query = "INSERT INTO utenti (nome, password) VALUES (%s, %s)"
        myCursor.execute(query, (self.nome, self.password))
        print("Utente registrato con successo.")

    def login(self):
        query = "SELECT * FROM utenti WHERE nome = %s AND password = %s"
        myCursor.execute(query, (self.nome, self.password))
        risultato = myCursor.fetchone()
        if risultato:
            self.id=risultato[0]
            print("Login effettuato con successo.")
            return True
        else:
            print("Credenziali errate.")
            return False
        
        
def menu_principale():
    while True:

        print("1. Registrati")
        print("2. Accedi")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            nome = input("Nome utente: ")
            password = input("Password: ")
            utente = Utente(nome, password)
            utente.registra()

        elif scelta == "2":
            nome = input("Nome utente: ")
            password = input("Password: ")
            utente = Utente(nome, password)
            if utente.login():
                menu_utente(utente)

        elif scelta == "3":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")

# Menu dopo login 
def menu_utente(utente):
    while True:
        print("1. Inserisci contatto")
        print("2. Visualizza contatti")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            inserisci_contatto(utente.id)
        elif scelta == "2":
            visualizza_contatti(utente.id)
        
        elif scelta == "3":
            print("Uscita")
            break
        else:
            print("Scelta non valida.")
            break

    

menu_principale()