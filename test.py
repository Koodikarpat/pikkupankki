from prohekti import nimiJaArvo, nimiarvovast

def rahanlisays(maara, nimi):
    tilinMaara = int(nimiJaArvo(nimi))
    tilinMaara = tilinMaara + maara
    print("Uusi määrä tilillä on " + str(tilinMaara))
    nimiarvovast(nimi, tilinMaara)

def rahanvahennys(maara, nimi):
    tilinMaara = int(nimiJaArvo(nimi))
    uusiMaara = tilinMaara - maara
    if uusiMaara>=0:
        print('uusi määrä tilillä on ' + str(uusiMaara))
        nimiarvovast(nimi, uusiMaara)

    else:
        print('tapahtuma hylätty')

def rahansiirto(nimi1, nimi2, maara = 5):
    tilin1maara = int(nimiJaArvo(nimi1))  # tähän funktio
    tilin2maara = int(nimiJaArvo(nimi2)) 

    if tilin1maara>=maara:
        tilin2maara = tilin2maara + tilin1maara
        nimiarvovast(nimi2, tilin2maara)
        nimiarvovast(nimi1, tilin1maara-maara)
    else:
        print('tapahtuma hylätty')

rahanlisays(20, "Oskari")
rahanvahennys(20, "Samuel")
rahansiirto('Kalle', 'Samuel', 20)