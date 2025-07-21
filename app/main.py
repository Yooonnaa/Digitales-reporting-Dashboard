import sys
from templates import transaktionen_file
from templates.transaktionen_file import neue_transaktion_erfassen

#Hauptliste
transaktionen = []
def startpoint():
    while True:
        print("Was möchtest du tun?")
        print("[1] Neue Einnahmen hinzufügen")
        print("[2] Neue Ausgabe hinzufügen")
        print("[0] Beenden")

        auswahl = input("Deine Auswahl: ")

        if auswahl == "1":
            transaktionen.append(neue_transaktion_erfassen("Einnahme"))
        elif auswahl == "2":
            transaktionen.append(neue_transaktion_erfassen("Ausgabe"))
        elif auswahl == "0":
            print("\nErfasste Transaktionen:")
            for t in transaktionen:
                print(t)
            print("Programm Beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine gültige Nummer.")


startpoint()