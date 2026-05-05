import pandas as pd
import glob

# Pronalazi sve CSV fajlove u folderu 'prodaja'
staza = r'./prodaja/*.csv'
svi_fajlovi = glob.glob(staza)

lista_tabela = []

for fajl in svi_fajlovi:
    # Učitavanje uz automatsko rešavanje problema sa zarezima/tačkama
    df = pd.read_csv(fajl, decimal=',') 
    lista_tabela.append(df)

# Spajanje u jednu veliku tabelu
glavna_tabela = pd.concat(lista_tabela, axis=0, ignore_index=True)

# Čišćenje: uklanjanje redova gde nema imena kupca i brisanje duplikata
glavna_tabela.dropna(subset=['Kupac'], inplace=True)
glavna_tabela.drop_duplicates(inplace=True)

# Čuvanje rezultata
glavna_tabela.to_excel('finalni_izvestaj.xlsx', index=False)
print("Sve tabele su spojene i očišćene!")
