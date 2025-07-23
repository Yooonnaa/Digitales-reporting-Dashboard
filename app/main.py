import sys
from templates import transaktionen_file
from templates.transaktionen_file import neue_transaktion_erfassen
from templates.transaktionen_file import transaktionen_aus_csv_laden
from templates.transaktionen_file import transaktionen_als_csv_speichern
from templates.transaktionen_file import gesamtsumme_einnahmen
from templates.transaktionen_file import gesamtsumme_ausgaben


transaktionen = transaktionen_aus_csv_laden()

# Start-Menü
def startpoint():
    while True:
        print("Was möchtest du tun?")
        # Auswahlmöglichkeiten
        print("[1] Neue Einnahmen hinzufügen")
        print("[2] Neue Ausgabe hinzufügen")
        print("[3] Gesamtsumme der Einnahmen")
        print("[4] Gesamtsumme der Ausgaben")
        print("[0] Beenden")

        auswahl = input("Deine Auswahl: ")

        if auswahl == "1":
            transaktionen.append(neue_transaktion_erfassen("Einnahme"))
            print("Einnahme Erfasst!")
        elif auswahl == "2":
            transaktionen.append(neue_transaktion_erfassen("Ausgabe"))
            print("Ausgabe Erfasst!")
        elif auswahl == "3":
            gesamtsumme_einnahmen()
        elif auswahl == "4":
            gesamtsumme_ausgaben()
        elif auswahl == "0":
            # Fragen ob Transaktionen gespeichert werden sollen
            transaktionspeichern = input("Möchtest du die Transaktionen als CSV Datei speichern? Y / N: ")
            if transaktionspeichern == "Y":
                transaktionen_als_csv_speichern(transaktionen)
            else:
                print("Transaktionen wurden nicht gespeichert.")
            print("Programm Beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine gültige Nummer.")



startpoint()