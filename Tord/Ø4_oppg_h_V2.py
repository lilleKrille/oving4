"""
h) Anta du har en plante som krever at temperaturen er +5 grader celsius for å vokse i det hele
tatt, og så vokser fortere desto varmere det er, lineært med temperatur over 5 grader. Skriv
en funksjon som regner ut summen av alle tall over 5 i lista. Så i lista [4, 7, 15] blir summen 0
(for 4) + 2 (for 7) + 10 (for 15)
"""
def sum_over_5 (liste_grader):
    sum = 0
    for temp in liste_grader:
        if temp > 5:
            sum += temp - 5
    return sum


liste_grader = [4,5,7,10,15]
Resultat_over_5 = sum_over_5(liste_grader)
print(Resultat_over_5)
