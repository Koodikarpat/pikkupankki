import sys
def tallentaminen():
    while True:
        userInput3 = input("Anna summa: ")
        if userInput3 > 0:
            mockuplisaus(userInput3)
            break

def nostaminen():
    while True:
        userInput4 = input("Anna summa: ")
        if userInput4 > 0:
            mockupnosto(userInput4)
            break

def siirtaminen():
    while True:
        userInput5 = input("Anna summa")
        if userInput5 > 0:
            mockupsiirto(userInput5)
            break

def lopeta():
    sys.exit()

def vaihtoehdot():
    while True:
        userInput2 = input("Anna komento: talleta, nosta, siirra, lopeta: ")
        if userInput2 == "talleta":
            tallentaminen()
        if userInput2 == "nosta":
            nostaminen()
        if userInput2 == "siirra":
            siirtaminen()
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
                vaihtoehdot()
                break   
            else:
                print("Vaara salasana!")




