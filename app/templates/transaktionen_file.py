import csv
import datetime

# Transaktionsvorlage
def neue_transaktion_erfassen(typ):
    date = datetime.datetime.now()
    transaktion= {
        "datum": date.strftime("%d.%m.%Y  %H:%M:%S"),
        "typ": typ,
        "betrag": float(input("Betrag: ")),
        "kategorie": input("Kategorie: "),
        "kommentar": input("Kommentar: "),
    }
    return transaktion


# Transaktion als CSV Speichern
def transaktionen_als_csv_speichern(transaktionen, dateiname="transaktionen.csv"):
    if not transaktionen:
        print("Keine Transaktionen zum Speichern")
        return

    feldnamen = transaktionen[0].keys()

    with open(dateiname, "w", newline="") as csv_datei:
        writer = csv.DictWriter(csv_datei, fieldnames=feldnamen)
        writer.writeheader()
        writer.writerows(transaktionen)

    print(f"Transaktionen wurden in {dateiname} gespeichert.")

# Transaktionen als CSV Laden
def transaktionen_aus_csv_laden(dateiname="transaktionen.csv"):
    try:
        with open(dateiname, "r") as csv_datei:
            reader = csv.DictReader(csv_datei)
            return list(reader)
    except FileNotFoundError:
        print(f"Datei {dateiname} nicht gefunden. Es werden keine Transaktionen geladen")
        return[]


