temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]

def sum_over_5 (liste_grader): #Funksjon som finner ut om temperaturene i listen er over 5 for så legge verdi over 5 i sum.
    sum = 0
    for temp in liste_grader:
        if temp > 5:
            sum += temp - 5
        elif temp < 0: #tar skade ved nagive grader
            sum += temp     
    return sum


liste_grader = temperaturer
Resultat_over_5 = sum_over_5(liste_grader)
print("Dersom vekst er gitt i cm tilsvarere dette: ", Resultat_over_5,"cm")
