def run():
    raumList = {}
    weitererRaum = True
    gesamtWohnung = 0
    anzahlRaum = 0

    while weitererRaum:
        teilrechteck = True
        gesamtRaum = 0

        print("Geben sie den Namen des Raumes an: ")
        nameRaum = input()

        while teilrechteck:
            print("Geben sie die Breite ihres Rechteckes/ Teilrechteckes an: ")
            breite = float(input())
            print("Geben sie nun die Länge an: ")
            laenge = float(input())

            gesamtRaum = gesamtRaum + (breite * laenge)

            print("Noch ein weiteres Teilrechteck?(Y/N)")
            userinput = input().lower()
            if userinput == "n":
                teilrechteck = False

        raumList.update({nameRaum: gesamtRaum})
        gesamtWohnung = gesamtWohnung + gesamtRaum
        anzahlRaum = anzahlRaum + 1

        print("Einen weiteren Raum? (Y/N) ")
        userinput = input().lower()
        if userinput == "n":
            weitererRaum = False

    raumDurchschnitt = gesamtWohnung / anzahlRaum

    for raum in raumList:
        print(f"{raum}: {raumList[raum]}")
    print(f"Gesamtgröße: {gesamtWohnung}m²")
    print(f"Durschnittsraumgröße: {raumDurchschnitt}m²")
