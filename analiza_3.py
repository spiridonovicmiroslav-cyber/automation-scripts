import pandas as pd

df = pd.read_excel('podaci_o_troskovima.xlsx')

# Osnovna statistika za kolonu 'Iznos'
statistika = df['Iznos'].describe()

# Detekcija ekstremnih vrednosti (Outliers) - pravilo 3 standardne devijacije
prosek = df['Iznos'].mean()
std_dev = df['Iznos'].std()

granica = prosek + 3 * std_dev
ekstremni_troskovi = df[df['Iznos'] > granica]

print("Osnovni parametri:")
print(statistika)
print(f"\nSumnjive transakcije iznad {granica:.2f} RSD:")
print(ekstremni_troskovi)
