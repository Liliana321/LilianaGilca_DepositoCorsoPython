'''
Serie Temporali: manipolazione dei dati 
'''
import pandas as pd
import numpy as np

# 1. Genera un intervallo di date (30 giorni consecutivi)
date_range = pd.date_range(start='2024-01-01', periods=30, freq='D')

# 2. Genera valori casuali (es. vendite)
valori = np.random.randint(10, 100, size=30)

# 3. Crea il DataFrame
df = pd.DataFrame({'Data': date_range, 'Vendite': valori})

# 4. Conversione della colonna 'Data' in datetime (già lo è, ma è buona pratica)
df['Data'] = pd.to_datetime(df['Data'])

# 5. Imposta la colonna 'Data' come indice
df.set_index('Data', inplace=True)

# 6. Resampling
df_daily = df.resample('D').mean()   # media giornaliera
df_monthly = df.resample('M').sum()  # somma mensile

# 7. Stampa i risultati
print("Media giornaliera:")
print(df_daily.head())

print("\nSomma mensile:")
print(df_monthly)


'''
Serve a spostare i valori verso il basso (o verso l'alto), utile per confronti temporali come 
differenze o variazioni percentuali.
'''
df['prev_day'] = df['Vendite'].shift(1)       # Valore del giorno precedente
df['daily_return'] = df['Vendite'].pct_change()  # Variazione percentuale giornaliera

'''
Calcola statistiche mobili su finestre temporali fisse. 
Utile per analisi di trend, volatilità, e smussamento dei dati.
'''

df['rolling_mean7'] = df['Vendite'].rolling(window=7).mean() # Media mobile su 7 giorni

df['rolling_std7'] = df['Vendite'].rolling(window=7).std()  # Deviazione standard mobile

# Visualizza le prime righe
print("\nSerie temporali con shift e rolling:")
print(df.head(10))