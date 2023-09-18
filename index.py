# g(x,y)
# reiknar ut kva trenden i eit datasett er. 
# Parameter: List X, Y
# kommentert ut kode som eg ikkje ser at me har bruk for
def g(x,y):
    teller, nevner = 0, 0
    print(nevner)
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

def i(temperaturliste):
    list = [0,0,0]
    for item in temperaturliste:
        if 20 <= item <25: 
            list[0] += 1
        elif 25 <= item < 30: 
            list[1] += 1
        elif 30 <= item:
            list[2] += 1
    print(f"sommerdager: {list[0]} høysommerdager: {list[1]} tropedager: {list[2]}")

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18,
21, 26, 21, 31, 15, 4, 1, -2]
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)

k(temperaturer_tidspunkter, temperaturer)
i(temperaturer)