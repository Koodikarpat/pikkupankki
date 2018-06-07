from prohekti import nimiJaArvo

def rahanlisays(maara, nimi):
    tilinMaara = nimiJaArvo(nimi)
    tilinMaara = tilinMaara + maara
    print("Uusi määrä tilillä on " + str(tilinMaara))

def rahanvahennys(maara, nimi):
    tilinMaara = nimiJaArvo(nimi)
    uusiMaara = tilinMaara - maara
    if uusiMaara>=0:
        print('uusi määrä tilillä on ' + str(uusiMaara))

    else:
        print('tapahtuma hylätty')

def rahansiirto(nimi, nimi2, maara = 5):
    tilin1maara = nimiJaArvo(nimi)  # tähän funktio
    tilin2maara = nimiJaArvo(nimi2) 

    if tilin1maara>=maara:
        tilin2maara = tilin2maara + tilin1maara
    else:
        print('tapahtuma hylätty')

rahanlisays(20, "Oskari")
rahanvahennys(20, "Samuel")
rahansiirto('Kalle', 'Samuel', 20)