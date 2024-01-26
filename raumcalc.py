def run():
    raum_list = {}
    weiterer_raum = True
    gesamt_wohnung = 0
    anzahl_raum = 0

    while weiterer_raum:
        teilrechteck = True
        gesamt_raum = 0

        print("Geben sie den Namen des Raumes an: ")
        name_raum = input()

        while teilrechteck:
            print("Geben sie die Breite ihres Rechteckes/ Teilrechteckes an: ")
            breite = float(input())
            print("Geben sie nun die Länge an: ")
            laenge = float(input())

            gesamt_raum = gesamt_raum + (breite * laenge)

            print("Noch ein weiteres Teilrechteck?(Y/N)")
            userinput = input().lower()
            if userinput == "n":
                teilrechteck = False

        raum_list.update({name_raum: gesamt_raum})
        gesamt_wohnung = gesamt_wohnung + gesamt_raum
        anzahl_raum = anzahl_raum + 1

        print("Einen weiteren Raum? (Y/N) ")
        userinput = input().lower()
        if userinput == "n":
            weiterer_raum = False

    raum_durchschnitt = gesamt_wohnung / anzahl_raum

    for raum in raum_list:
        print(f"{raum}: {raum_list[raum]}")
    print(f"Gesamtgröße: {gesamt_wohnung}m²")
    print(f"Durschnittsraumgröße: {raum_durchschnitt}m²")


