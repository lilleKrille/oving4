#Listene som ble oppgitt i oppgaven
liste_grader = [4,5,7,10,15]
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
testListeFlyttall = [-16.5, 14.9, -11.5, 18.4, 7.0, -4.3, 0.5, 1.2, 1.4, -1.1, 
                     -12.4, 19.0, 7.6, -3.9, 9.4, 0.1, 9.2, -3.5, 10.1, 7.5]

# g(x,y)
# reiknar ut kva trenden i eit datasett er. 
# Parameter: List X, Y
# kommentert ut kode som eg ikkje ser at me har bruk for
def g(x,y):
    teller, nevner = 0, 0
    snittX = snitt(x)
    snittY = snitt(y)
    for i in range(len(x)):
        teller += (x[i]-snittX)*(y[i]-snittY)
        nevner += (x[i]-snittX)**2
    a = teller/nevner
#    b = snittY - a*snittX
    return a#, b

#reiknar snittet til ei liste
def snitt(liste):
    snitt = 0
    for item in liste:
        snitt += item
    return snitt/len(liste)

def k(x,y):
    a = g(x,y)
    if a < 0:   print("trenden er negativ")
    elif a > 0: print("trenden er positiv")
    else:       print("ingen trend")

#brukar funksjonen antallElementerStorreEllerLik() til å finna dagar med ein gitt temperatur
def i(temperaturliste):
    typeDager = [0,0,0]
    for i in range(20, 31, 5):
        typeDager[i%4] = antallElementerStorreEllerLik(temperaturliste, i)
    print(f"sommerdager: {typeDager[0]} høysommerdager: {typeDager[1]} tropedager: {typeDager[2]}")

#Funksjon som tar inn ei liste med flyttall og en verdi. Funksjonen skal telle antall elementer i lista
#som er større eller lik verdien som er oppgitt og deretter returnere antallet
def antallElementerStorreEllerLik(aListe, aVerdi):
    antall = 0
    for i in aListe:
        if i >= aVerdi:
            antall += 1
    return antall

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
  
def sum_over_5 (liste_grader): #Funksjon som finner ut om temperaturene i listen er over 5 for så legge verdi over 5 i sum.
    sum = 0
    for temp in liste_grader:
        if temp > 5:
            sum += temp - 5
        elif temp < 0: #tar skade ved nagive grader
            sum += temp     
    return sum
  
def sum_over_5 (liste_grader): #Funksjon som finner ut om temperaturene i listen er over 5 for så legge verdi over 5 i sum.
    sum = 0
    for temp in liste_grader:
        if temp > 5:
            sum += temp - 5
    return sum



Resultat_over_5 = sum_over_5(liste_grader)
print(Resultat_over_5)

#Oppgave m) Bruk funksjonen fra oppgave f) på den oppgitte lista «døgn-nedbør» for å finne den lengste perioden uten nedbør
print(f"Den lengste perioden uten nedbør varte i {lengdeLengsteSekvens(dogn_nedbor)} dager")

temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)
    
i(temperaturer)

liste_grader = temperaturer
Resultat_over_5 = sum_over_5(liste_grader)
print("Dersom vekst er gitt i cm tilsvarere dette: ", Resultat_over_5,"cm")
