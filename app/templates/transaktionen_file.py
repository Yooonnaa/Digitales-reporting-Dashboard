import datetime


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



