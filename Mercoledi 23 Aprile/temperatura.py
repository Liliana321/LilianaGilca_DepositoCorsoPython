
'''
temperatura:

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Genera 31 valori casuali tra 15 e 40 
temperature = np.random.randint(15, 40, size=31)

# Crea un DataFrame
df = pd.DataFrame({'Temperatura': temperature}, index=range(1,32))
print(df.head())

def statistiche():
    max_temp=df["Temperatura"].max()
    min_temp=df["Temperatura"].min()
    mean_temp=df["Temperatura"].mean()
    median_temp=df["Temperatura"].median()
    print(f"La temperatura massima è {max_temp}")
    print(f"La temperatura minima è {min_temp}")
    print(f"La temperatura media è {mean_temp}")
    print(f"La mediana è {median_temp}")

statistiche()

# # grafico a linee
# plt.plot(df['Temperatura'])
# plt.title('Andamento della Temperatura')
# plt.xlabel('Giorno')
# plt.ylabel('Temperatura (°C)')
# plt.grid(True)
# plt.show()


def mostra_grafici(df):
    giorni = df.index # indici da 1 a 31 rappresentano i giorni del mese  --> ASSE X
    temperatura = df['Temperatura'] #input colonna df --> ASSE Y 
    media = temperatura.mean()

    plt.figure(figsize=(12, 5))

    # Grafico a linee
    plt.subplot(1, 2, 1)
    plt.plot(giorni, temperatura, marker='o')
    plt.axhline(media,color="green",linewidth=1) # linewidth=1 linea sottile 
    plt.title('Grafico a Linee')
    plt.xlabel('Giorno') 
    plt.ylabel('Temperatura °C')
    plt.grid(True)

    # Scatter plot: i punti rappresentano la temperatura 
    plt.subplot(1, 2, 2)
    plt.scatter(giorni, temperatura, color='red')
    plt.axhline(media,color="green",linewidth=1)
    plt.title('Scatter Plot')
    plt.xlabel('Giorno')
    plt.ylabel('Temperatura °C')
    plt.grid(True)

    plt.tight_layout() # ottimizza la disposizione dei grafici per evitare sovrapposizioni.
    plt.show()

mostra_grafici(df)