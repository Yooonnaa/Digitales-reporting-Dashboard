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

# Transaktionen aus CSV Laden
def transaktionen_aus_csv_laden(dateiname="transaktionen.csv"):
    try:
        with open(dateiname, "r") as csv_datei:
            reader = csv.DictReader(csv_datei)
            transaktionen = []
            #Umwandeln von String in Float für den Betrag
            for row in reader:
                row["betrag"] = float(row["betrag"])
                transaktionen.append(row)
            return list(reader)
    except FileNotFoundError:
        print(f"Datei {dateiname} nicht gefunden. Es werden keine Transaktionen geladen")
        return[]

# Gesamtsumme der Einnahmen berechnen
def gesamtsumme_einnahmen():
    with open("transaktionen.csv", "r") as csv_datei:
        csv_reader = csv.DictReader(csv_datei)
        line_count = 0
        gesamtsumme = 0
        for row in csv_reader:
            if row["typ"] == "Einnahme":
                row["betrag"] = float(row["betrag"])
                gesamtsumme += row["betrag"]
                line_count += 1
        #Gibt den Wert der Gesamtsumme aus in €
        print(f"Gesamtsumme der Einnahmen: {gesamtsumme:.2f}")
        #Zeigt an wie viele Reihen bearbeitet wurden.
        print(f"Processed {line_count} line(s).")


# Gesamtsumme der Ausgaben berechnen
def gesamtsumme_ausgaben():
    with open("transaktionen.csv", "r") as csv_datei:
        csv_reader = csv.DictReader(csv_datei)
        line_count = 0
        gesamtsumme = 0
        for row in csv_reader:
            if row["typ"] == "Ausgabe":
                row["betrag"] = float(row["betrag"])
                gesamtsumme += row["betrag"]
                line_count += 1
        #Gibt den Wert der Gesamtsumme aus in €
        print(f"Gesamtsumme der Ausgaben: {gesamtsumme:.2f}")
        #Zeigt an wie viele Reihen bearbeitet wurden.
        print(f"Processed {line_count} line(s).")

# Bilanz Berechnen
