#Listene som ble oppgitt i oppgaven
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
testListeFlyttall = [-16.5, 14.9, -11.5, 18.4, 7.0, -4.3, 0.5, 1.2, 1.4, -1.1, 
                     -12.4, 19.0, 7.6, -3.9, 9.4, 0.1, 9.2, -3.5, 10.1, 7.5]

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

#Oppgave m) Bruk funksjonen fra oppgave f) på den oppgitte lista «døgn-nedbør» for å finne den lengste perioden uten nedbør
print(f"Den lengste perioden uten nedbør varte i {lengdeLengsteSekvens(dogn_nedbor)} dager")
