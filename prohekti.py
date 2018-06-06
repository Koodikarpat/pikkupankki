def getIndex(raakaTeksti):
    u = 0
    for i in raakaTeksti:
        if i == ":":
            break
        else:
            u += 1
    return u

def otaNimi(raakaTeksti):
    return raakaTeksti[:getIndex(raakaTeksti)]

def otaMaara(raakaTeksti):
    return raakaTeksti[getIndex(raakaTeksti)+1:]

# lyukee tiedoston läpi ja etsii halutun henkilön. jos ei löydy lisää henkilön listaan. 
# käy tiedoston läpi ja katsoo onko siellä tiettyä nimeä ja kertoo sen r0ahamäärän#
#  kirjoittaa kokonaan tiedoston uudestaan 
# lukea riviltä
# ottaa vastaan nimen ja palauttaa 

def nimihaku(nimi):
    nimilöyty = False
    avaus = open('D:/Lisäohjelmat/pythno/Lib/site-packages/testii.txt','r')
    for i in avaus.readlines():
        if otaNimi(i) == nimi:
            nimilöyty = True
            print(i)
    avaus.close()
    if nimilöyty == False:
        appendFile = open('D:/Lisäohjelmat/pythno/Lib/site-packages/testii.txt','a')
        appendFile.write("\n"+nimi+":0")
        appendFile.close()
nimihaku("antti")

def nimiJaArvo(nimi):
    nimilöyty1 = False
    avaus1 = open('D:/Lisäohjelmat/pythno/Lib/site-packages/testii.txt','r')
    for i in avaus1.readlines():
        if otaNimi(i) == nimi:
            nimilöyty1 = True
            print(otaMaara(i))
    avaus1.close()

nimiJaArvo('Matias')

teksti = 'Hieno teksti yeyeyeyee'
uusKir = open('D:/Lisäohjelmat/pythno/Lib/site-packages/testii2.txt','w')
uusKir.write(teksti)
uusKir.close

luku = open('D:/Lisäohjelmat/pythno/Lib/site-packages/testii.txt','r')
print(luku.readlines())

tekst = 'arvo'

def nimihaku2(nimi):
    nimilöyty2 = False
    avaus2 = open('D:/Lisäohjelmat/pythno/Lib/site-packages/testii.txt','r')
    for i in avaus2.readlines():
        if otaNimi(i) == nimi:
            nimilöyty2 = True
            print(i)
    avaus2.close()
    if nimilöyty2 == True:
        print('ee')
