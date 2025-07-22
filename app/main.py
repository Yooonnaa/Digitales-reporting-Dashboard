import sys
from templates import transaktionen_file
from templates.transaktionen_file import neue_transaktion_erfassen
from templates.transaktionen_file import transaktionen_aus_csv_laden
from templates.transaktionen_file import transaktionen_als_csv_speichern

transaktionen = transaktionen_aus_csv_laden()

# Start-Menü
def startpoint():
    while True:
        print("Was möchtest du tun?")
        # Auswahlmöglichkeiten
        print("[1] Neue Einnahmen hinzufügen")
        print("[2] Neue Ausgabe hinzufügen")
        print("[0] Beenden")

        auswahl = input("Deine Auswahl: ")

        if auswahl == "1":
            transaktionen.append(neue_transaktion_erfassen("Einnahme"))
            print("Einnahme Erfasst!")
        elif auswahl == "2":
            transaktionen.append(neue_transaktion_erfassen("Ausgabe"))
            print("Ausgabe Erfasst!")
        elif auswahl == "0":
            transaktionen_als_csv_speichern(transaktionen)
            print("Programm Beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine gültige Nummer.")


startpoint()