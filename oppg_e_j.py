"""
e)
Skriv en funksjon som tar inn ei liste med tall. For hvert tall i lista unntatt det siste skal
funksjonen regne ut differansen mellom neste tall i lista og dette tallet. Differansene skal
legges inn i ei ny liste

j)
Bruk funksjonen fra oppgave e) til å finne ut om temperaturen er stigende eller synkende for
hvert tidspunkt. Gå gjennom lista som dere får når dere kaller funksjonen fra oppgave e) på
temperaturlista. For hvert element skriv ut indeksen og skriv ut «stigende» om differansen er
over 0, «synkende» om den er negativ eller «uforandret» om den er 0.
"""

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]

# e)
def beregne_differanser(liste):
    differanser = []
    for i in range(1,len(liste)):
        diff = liste[i]-liste[i-1]
        differanser.append(diff)
    return differanser



diffs = beregne_differanser(temperaturer)
print(diffs)

#j)
for index in range(len(diffs)):
    if diffs[index] > 0:
        print(f"Stigende for index: {index}")
    elif diffs[index] < 0:
        print(f"Synkende for index: {index}")
    else:
        print(f"Uforandret for index: {index}")



