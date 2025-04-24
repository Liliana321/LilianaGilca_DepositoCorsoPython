import pandas as pd

'''Creazione di un DataFrame che deve includere:
-data 
-citta: 3
-prodotto: 3 
-vendite  per periodo di mese 


'''
import numpy as np


città=["Roma","Pescara","Firenze"]
prodotto=["Vernice","Pasta","Vestiti"]
data=pd.date_range("1-03-2025","31-03-2025")

# dati=[]

# for i in data:
#     for c in città:
#         for j in prodotto:
#             vendita=np.random.randint(20,100)
#             dati.append([i,j,c,vendita])
            
          
# df = pd.DataFrame(dati, columns=['Data', 'Città', 'Prodotto', 'Vendite'])

# print(df.head())


# Lista delle città possibili


# Generazione casuale size10
vettore_città = np.random.choice(città, size=10)
vettore_prodotto = np.random.choice(prodotto, size=10)
vettore_data = np.random.choice(data, size=10)
vettore_vendita=np.random.randint(20,100,size=10)

# Costruzione del DataFrame 
dati_vec = [vettore_data, vettore_città, vettore_prodotto, vettore_vendita]
df_vec = pd.DataFrame(np.array(dati_vec).T, columns=['Data', 'Città', 'Prodotto', 'Vendite'])

print(df_vec.head())

# tabella pivot

table_pivot=df_vec.pivot_table(
    index='Prodotto',     # Riga
    columns='Città',      # Colonna
    values='Vendite',     
    aggfunc='sum',        
    fill_value=0   #missing==0
)

print(table_pivot) # totale vendite per ogni citta e prodotto 
# Creazione della tabella pivot
table_mean_pivot=df_vec.pivot_table(
    index='Prodotto',     # Riga
    columns='Città',      # Colonna
    values='Vendite',     
    aggfunc='mean',        
    fill_value=0   #missing==0
)

print(table_mean_pivot)

# vendite totali per prodotto
vendite_per_prodotto = df_vec.groupby('Prodotto')['Vendite'].sum().reset_index()
print(vendite_per_prodotto)



df_vec_resampled = df_vec.resample('M').mean()
