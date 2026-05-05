import googlemaps
import pandas as pd

# Inicijalizacija klijenta sa API ključem
gmaps = googlemaps.Client(key='TVOJ_API_KLJUC')

def uzmi_milje(red):
    try:
        rezultat = gmaps.distance_matrix(red['Pocetna_Adresa'], red['Krajnja_Adresa'], mode='driving', units='imperial')
        # Izvlačenje vrednosti u miljama iz JSON odgovora
        milje_tekst = rezultat['rows'][0]['elements'][0]['distance']['text']
        return milje_tekst
    except:
        return "Greška"

# Učitavanje tabele sa adresama
df = pd.read_csv('logistika.csv')

# Primena funkcije na svaki red u tabeli
df['Razdaljina_Milje'] = df.apply(uzmi_milje, axis=1)

df.to_csv('logistika_sa_razdaljinama.csv', index=False)
