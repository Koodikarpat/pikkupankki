from prohekti import nimiJaArvo, nimiarvovast

def rahanlisays(maara, nimi):
    tilinMaara = int(nimiJaArvo(nimi))
    tilinMaara = tilinMaara + maara
    print(tilinMaara)
    print("Uusi määrä tilillä on " + str(tilinMaara))
    nimiarvovast(tilinMaara, nimi)

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
        nimiarvovast(tilin2maara + maara, nimi2)
        nimiarvovast(tilin1maara-maara, nimi1)
    else:
        print('tapahtuma hylätty')