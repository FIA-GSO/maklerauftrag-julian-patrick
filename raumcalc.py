import re


def run():
    raum_list = {}
    weiterer_raum = True
    gesamt_wohnung = 0
    anzahl_raum = 0

    # Solange Raum vorhanden, berechne Größe
    while weiterer_raum:
        teilrechteck = True
        gesamt_raum = 0
        print("Geben sie den Namen des Raumes an: ")
        name_raum = name_input()

        gesamt_raum = calc_teilrechteck(gesamt_raum, teilrechteck)
        raum_list.update({name_raum: gesamt_raum})
        gesamt_wohnung = gesamt_wohnung + gesamt_raum
        anzahl_raum = anzahl_raum + 1

        # Abfrage ob weiterer Raum vorhanden
        print("Einen weiteren Raum? (Y/N) ")
        userinput = yes_no_input()
        if userinput == "n":
            weiterer_raum = False

    raum_durchschnitt = gesamt_wohnung / anzahl_raum
    print_list(gesamt_wohnung, raum_durchschnitt, raum_list)


# Berechnet Teilrechtecke solange vorhanden
def calc_teilrechteck(gesamt_raum, teilrechteck):
    while teilrechteck:
        print("Geben sie die Breite ihres Rechteckes/ Teilrechteckes an: ")
        breite = float(number_input())
        print("Geben sie nun die Länge an: ")
        laenge = float(number_input())

        gesamt_raum = gesamt_raum + (breite * laenge)

        print("Noch ein weiteres Teilrechteck?(Y/N)")
        userinput = yes_no_input()
        if userinput == "n":
            teilrechteck = False
    return gesamt_raum


# Ausgabe der Ergebnisse in Listenform für Anschaulichkeit
def print_list(gesamt_wohnung, raum_durchschnitt, raum_list):
    for raum in raum_list:
        print(f"{raum}: {raum_list[raum]}m²")
    print(f"Gesamtgröße: {gesamt_wohnung}m²")
    print(f"Durschnittsraumgröße: {raum_durchschnitt}m²")


def yes_no_input():
    pattern = re.compile(r"[yYnN]")
    not_matching = True
    while not_matching:
        eingabe = input()
        if pattern.match(eingabe):
            return eingabe.lower()
        else:
            print("Falsche Eingabe, bitte erneut eingeben: (Y/N)")


def number_input():
    integer = re.compile(r"\d+")
    floating = re.compile(r"\d+[.]\d+")
    not_matching = True
    while not_matching:
        zahl = input()
        if integer.match(zahl) or floating.match(zahl):
            return zahl
        else:
            print("Falsche Eingabe, bitte erneut eingeben: (Ganz- oder Dezimalzahl)")


def name_input():
    pattern = re.compile(r"^[a-zA-ZöäüÄÖÜ]+$")
    not_matching = True
    while not_matching:
        name = input()
        if pattern.match(name):
            return name
        else:
            print("Falsche Eingabe, bitte erneut eingeben: ")
