from datetime import datetime
import matplotlib.pyplot as plt

# e og j- Anders
def beregne_differanser(liste):
    differanser = []
    for i in range(1,len(liste)):
        diff = liste[i]-liste[i-1]
        differanser.append(diff)
    return differanser

def StigendeSynkende():
    diffs = beregne_differanser(temperaturer)
    print(diffs)
    for index in range(len(diffs)):
        if diffs[index] > 0:
            print(f"Stigende for index: {index}")
        elif diffs[index] < 0:
            print(f"Synkende for index: {index}")
        else:
            print(f"Uforandret for index: {index}")

#oppgåve f og m Lukas
#Funksjon som tar inn ei liste med flyttall og en verdi. Funksjonen skal telle antall elementer i lista
#som er større eller lik verdien som er oppgitt og deretter returnere antallet
#Funksjon som tar inn ei liste med tall og en verdi. Funksjonen skal lete i lista og returnere 
#lengden til den lengste sammenhengende sekvensen av verdien som er oppgitt.
#Hvis man ikke skriver inn en verdi vil funksjonen som standard lete etter lengste sekvens av 0-ere
def lengdeLengsteSekvens(aListe, aVerdi = 0):
    lengsteSekvens = 0
    sekvens = 0
    for i in aListe:
        if i == aVerdi:
            sekvens += 1
            if sekvens > lengsteSekvens:
                lengsteSekvens = sekvens
        else:
            sekvens = 0
    return lengsteSekvens

#oppgåve g og k- Kristoffer
# g(x,y)
# reiknar ut kva trenden i eit datasett er. 
# Parameter: List X, Y
# kommentert ut kode som eg ikkje ser at me har bruk for
def g(x,y):
    teller, nevner = 0, 0
    snittX = sum(x)/len(x)
    snittY = sum(y)/len(y)
    for i in range(len(x)):
        teller += (x[i]-snittX)*(y[i]-snittY)
        nevner += (x[i]-snittX)**2
    a = teller/nevner
#    b = snittY - a*snittX
    return a#, b

#Sjekkar om ein trend.
def k(x,y):
    a = g(x,y)
    if a < 0:   print("trenden er negativ")
    elif a > 0: print("trenden er positiv")
    else:       print("ingen trend")


#oppgåve d og i - Lukas og Kristoffer
def antallElementerStorreEllerLik(aListe, aVerdi):
    antall = 0
    for i in aListe:
        if i >= aVerdi:
            antall += 1
    return antall
#brukar funksjonen antallElementerStorreEllerLik() til å finna dagar med ein gitt temperatur
def i(temperaturliste):
    typeDager = [0,0,0]
    for i in range(20, 31, 5):
        typeDager[i%4] = antallElementerStorreEllerLik(temperaturliste, i)
    print(f"sommerdager: {typeDager[0]} høysommerdager: {typeDager[1]} tropedager: {typeDager[2]}")



  
#oppgåve h og L - tord
def sum_over_5 (liste_grader): #Funksjon som finner ut om temperaturene i listen er over 5 for så legge verdi over 5 i sum.
    sum = 0
    for temp in liste_grader:
        if temp > 5:
            sum += temp - 5
        elif temp < 0: #tar skade ved nagive grader
            sum += temp     
    return sum

#Listene som ble oppgitt i oppgaven
liste_grader = [4,5,7,10,15]
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
testListeFlyttall = [-16.5, 14.9, -11.5, 18.4, 7.0, -4.3, 0.5, 1.2, 1.4, -1.1, 
                     -12.4, 19.0, 7.6, -3.9, 9.4, 0.1, 9.2, -3.5, 10.1, 7.5]
temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)

#oppgåve I) Finn antall sommerdager (over 20), høysommerdager (over 25) og tropedager (over 30).
i(temperaturer)

#oppgåve j) 
StigendeSynkende()

#oppgåve K) Bruk funksjonen fra oppgave g) for å finne trenden i temperaturlista.
k(temperaturer_tidspunkter, temperaturer)

#L
liste_grader = temperaturer
Resultat_over_5 = sum_over_5(liste_grader)
print("Dersom vekst er gitt i cm tilsvarere dette: ", Resultat_over_5,"cm")

#Oppgave m) Bruk funksjonen fra oppgave f) på den oppgitte lista «døgn-nedbør» for å finne den lengste perioden uten nedbør
print(f"Den lengste perioden uten nedbør varte i {lengdeLengsteSekvens(dogn_nedbor)} dager")



#Øving 10

#Oppgave a, Henter data fra valgfri fil
def lesFraFil(aFilnavn):
    navn = list()
    stasjon = list()
    dato = list()
    snodybde = list()
    nedbor = list()
    middeltemperatur = list()
    snittSkydekke = list()
    middelvind = list()

    with open(aFilnavn, "r") as file:
        lines = file.readlines()
        lines = lines[1:-1]                 #Skipper første og siste linje 

        for line in lines:
            lineData = line.split(";")

            navn.append(lineData[0])
            stasjon.append(lineData[1])

            datoString = lineData[2]
            datoObjekt = datetime.strptime(datoString, "%d.%m.%Y")
            datoObjekt = datoObjekt.date()
            dato.append(datoObjekt)

            snodybde.append(lineData[3])
            nedbor.append(lineData[4])
            middeltemperatur.append(lineData[5])
            snittSkydekke.append((lineData[6].replace(",", "."),datoObjekt ))
            middelvind.append(lineData[7].strip("\n"))
            
    data = dict()
    data["navn"] = navn
    data["stasjon"] = stasjon
    data["dato"] = dato
    data["snodybde"] = snodybde
    data["nedbor"] = nedbor
    data["middeltemperatur"] = middeltemperatur
    data["snittSkydekke"] = snittSkydekke
    data["middelvind"] = middelvind

    return data

#Oppgave b, går gjennom datoer med data for snødybde og returnerer lister for hvert år med antall skiføredager
def skiforeDager(aDatoListe, aSnodybdeListe):
    skisesonger = dict()
    sesongString = list()
    hasCleared = False
    
    if(aDatoListe[0].month < 10):
        year = aDatoListe[0].year - 1
    else:
        year = aDatoListe[0].year
    
    for i, dato in enumerate(aDatoListe):
        if (dato.year == year and dato.month >= 10) or (dato.year == year + 1 and dato.month < 6):
            if hasCleared: 
                hasCleared = False

            sesongString.append(aSnodybdeListe[i])
        else:
            if not hasCleared:
                sesong = list()
                
                for i in sesongString:
                    try:
                        sesong.append(float(i))
                    except ValueError:
                        pass
            
                if not len(sesong) == 0:
                    skisesonger[year] = antallElementerStorreEllerLik(sesong, 20)
                
                sesong.clear()
                sesongString.clear()
                hasCleared = True
                year += 1
                

    return skisesonger

#oppgåve d) 
#graferSkiføre(x,y) - plottar trend og faktisk skiføre kvart år 
#Parameter:
#   [list] x = år
#   [list] y = dagar med skiføre
#ingen returverdi
def graferSkiføre(x,y):
    trend = g(x,y) #oppgåve c), returnerer ei liste med stigningstal og konstantledd for trenden
    trendGraf = []
    trendGraf.append(f(trend[0], trend[1], 0))
    trendGraf.append(f(trend[0], trend[1], ))
    xi = len(x)
    plt.plot(x,y, label="Dagar med skiføre kvart år")
    plt.plot([0, xi], trendGraf, label="Trend")
    plt.show()

#lineær funkjon
def f(a,b,x): return a*x+b 

##utføring av kode
datasett = lesFraFil("snoedybder_vaer_en_stasjon_dogn.csv")
#oppgåve c)
#x = år, y = antall dager med skiføre
