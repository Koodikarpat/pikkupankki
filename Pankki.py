import sys
def tallentaminen(nimi):
    while True:
        userInput3 = int(input("Anna summa: "))
        if userInput3 > 0:
            mockuplisaus(nimi, userInput3)
            break

def nostaminen(nimi):
    while True:
        userInput4 = int(input("Anna summa: "))
        if userInput4 > 0:
            mockupnosto(nimi, userInput4)
            break

def siirtaminen(nimi):
    while True:
        userInput5 = input ("Anna saajan nimi: ")
        if userInput5 == "":
            pass
        else:
            while True:
                userInput6 = int(input("Anna summa:"))
                if userInput6 > 0:
                    mockupsiirto(nimi, userInput5)
                    break

def lopeta():
    sys.exit()

def vaihtoehdot(nimi):
    while True:
        userInput2 = input("Anna komento: talleta, nosta, siirra, lopeta: ")
        if userInput2 == "talleta":
            tallentaminen(nimi)
        if userInput2 == "nosta":
            nostaminen(nimi)
        if userInput2 == "siirra":
            siirtaminen(nimi)
        if userInput2 == "lopeta":
            lopeta()

tunnus = 'ss'

salasana = 'TESTI'

while True:
    userInput0 = input("Anna nimi: ")
    if userInput0 == "":
        pass
    else: 
        while True:
            userInput1 = input("Anna salasana: ")
            if userInput1 == salasana:
                print('Tervetuloa,'+ userInput0)
                vaihtoehdot(userInput0)
                break   
            else:
                print("Vaara salasana!")




