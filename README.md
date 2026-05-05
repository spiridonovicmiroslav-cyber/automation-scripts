# automation-scripts
# Business Process Automation & Data Analysis Tools 📊🚀

Ovaj repozitorijum sadrži set Python alata dizajniranih za automatizaciju svakodnevnih poslovnih zadataka i naprednu analizu podataka. Fokus je na uštedi vremena i smanjenju ljudskih grešaka u radu sa velikim setovima podataka.

## 🛠 Glavne Funkcionalnosti

### 1. Automated Data Merger & Cleaner
*   **Problem:** Klijenti često imaju podatke razbacane u desetinama CSV/Excel fajlova sa različitim formatima brojeva.
*   **Rešenje:** Skripta automatski skenira folder, spaja sve tabele u jednu, rešava probleme sa regionalnim podešavanjima (tačka/zarez) i uklanja duplikate.
*   **Tehnologije:** `Pandas`, `Glob`.

### 2. Geographic Distance Calculator (Logistics Tool)
*   **Problem:** Ručno računanje razdaljina za stotine adresa radi obračuna troškova transporta.
*   **Rešenje:** Skripta koja koristi Google Maps API za automatsko izračunavanje razdaljine u miljama/kilometrima direktno iz Google Sheets tabele.
*   **Tehnologije:** `Google Maps API`, `Python`.

### 3. Statistical Outlier Detection
*   **Problem:** Identifikacija sumnjivih transakcija ili grešaka u unosu u velikim finansijskim izveštajima.
*   **Rešenje:** Primena statističkih metoda (Standardna devijacija i ANOVA) za automatsko markiranje anomalija.
*   **Tehnologije:** `Scipy`, `Numpy`.

## 🚀 Kako koristiti ove skripte
1. Klonirajte repozitorijum.
2. Instalirajte potrebne biblioteke: `pip install pandas googlemaps openpyxl`.
3. Pokrenite glavnu skriptu ili koristite priložene Jupyter (Google Colab) sveske za interaktivni rad.

---
**Kontakt:** Ukoliko vam je potrebna prilagođena automatizacija za vaš biznis, slobodno me kontaktirajte putem Upwork profila.
