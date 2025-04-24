'''
Utilizzare Pandas e NumPy per esplorare, pulire, trasformare e analizzare un dataset di clienti di una compagnia di
telecomunicazioni. L’obiettivo finale è costruire un modello predittivo di base per la churn rate (abbandono del cliente) 
e scoprire correlazioni tra vari attributi del cliente e la sua fedeltà.
'''

'''
Il dataset contiene le seguenti colonne:

ID_Cliente: Identificativo unico per ogni cliente

Età: Età del cliente

Durata_Abbonamento: Quanti mesi il cliente è stato abbonato

Tariffa_Mensile: Quanto il cliente paga al mese

Dati_Consumati: GB di dati consumati al mese

Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti

Churn: Se il cliente ha lasciato la compagnia (valori: "Sì" o "No")

'''

'''
1. Caricamento e Esplorazione Iniziale:
Caricare i dati da un file CSV.

Usare le funzioni info(), describe() e value_counts() per esplorare la distribuzione dei dati e
identificare eventuali colonne con valori mancanti.
'''

import pandas as pd
import numpy as np





df= pd.read_csv('churn.csv')

#dataset.to_csv('dataframe_churn.csv', index=False)

#  Esplorazione iniziale
print("=== INFO ===")
print(df.info())
print("\n=== DESCRIZIONE ===")
print(df.describe())
print("\n=== DISTRIBUZIONE CHURN ===")
print(df['Churn'].value_counts())



#  Creazione colonna derivata: Costo_per_GB
df['Costo_per_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']
# modifica churn 
df['Churn_Num'] = df['Churn'].replace({'Sì': 1, 'No': 0})
print("\n=== Prime righe del dataset aggiornato ===")
print(df.head())

#  Analisi Esplorativa dei Dati
esplorazione= df.groupby('Churn')[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Costo_per_GB']].mean()
correlazione=df.corr(numeric_only=True)
# --- Salvataggio su file CSV ---
esplorazione.to_csv("esplorazione_churn.csv")
correlazione.to_csv("correlazione_churn.csv")

#corr positiva--> tariffa mensile e costo per GB 0.29 : 
#tariffa mensile cresce--> cresce il costo per GB.

#corr neg dati_consumati e costo per GB
#Più consumi--> minore costo per GB

# --- Selezione delle colonne numeriche da normalizzare ---
colonne = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati',
            'Servizio_Clienti_Contatti', 'Costo_per_GB']

# Normalizzazione con (x-µ)/sd

df[colonne] = (df[colonne] - df[colonne].mean()) / df[colonne].std()


# Mostra le prime righe
print(df.head())

# Salvataggio del DataFrame normalizzato
df.to_csv("churn_normalizzato.csv", index=False)



# Caricamento del dataset preparato
df = pd.read_csv("churn_normalizzato.csv")


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score


X = df[colonne] #variabili per predire churn
y = df['Churn_Num'] 

# Divisione train-test (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modello di regressione logistica e addestramentyo 
modello = LogisticRegression()
modello.fit(X_train, y_train)

# Predizione
y_pred = modello.predict(X_test)
y_prob = modello.predict_proba(X_test)[:, 1] #probabilità che un cliente faccia churn 

# Valutazione del modello
accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_prob)

print(f"Accuratezza: {accuracy:.2f}")
print(f"AUC: {auc:.2f}")