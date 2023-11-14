from datetime import datetime
import matplotlib.pyplot as plt


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
            middeltemperatur.append((lineData[5].replace(",", "."), datoObjekt)) # legg til dato i dict, og erstatt , med .
            snittSkydekke.append((lineData[6].replace(",", "."),datoObjekt )) # legg til dato i dict, og erstatt , med .
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


def plot_penvaersdager(datasett):
    data = dict()
    #obj is (VALUE, DATE)         obj[0] = VALUE, obj[1] = DATE
    print(datasett)
    for obj in datasett:
        try:
            if obj[1].year in data:
                if float(obj[0]) <= 3:
                    data[obj[1].year] = data[obj[1].year] + 1
            else:
                if float(obj[0]) <= 3:
                    data[obj[1].year] = 1
        except ValueError: 
            continue

    plt.plot(list(data.keys()), list(data.values()), "o-")
    plt.show()


def beregne_differanser(liste):
    differanser = []
    for i in range(1,len(liste)):
        diff = liste[i]-liste[i-1]
        differanser.append(diff)
    return differanser
{ 
 "07/2020": [2,3,4,4,5,2,8],
 "2021": [3,2,5,6,4],
 "2022": 2,
 "2023": 1,
 "1980": 0,
 }
[2020, 2021, 2022, 2023, 1980]
[2,3,2,1,0]

def plot_temp_per_mnd(datasett):
    result = dict()
    for data in datasett:
        try:
            date = f"{data[1].month}/{data[1].year}"
            if date in result:
                result[date].append(float(data[0]))
            else:
                result[date] = [float(data[0])]
        except ValueError:
            continue

    # calculate average:
    result_avg = dict()
    for key in result:
        result_avg[key] = round(sum(result[key])/len(result[key]), 2)
    
    # Finn differanser:
    result_diff = beregne_differanser(list(result_avg.values()))

    # PLOT:
    plt.plot(list(result_avg.keys()),list(result_avg.values()), "o-", label="gjennomsnitt temperatur")
    plt.plot(list(result_avg.keys())[1:],result_diff, "o-", label="gjennomsnitt temperatur")
    plt.legend()
    plt.show()




if __name__ == "__main__":
    datasett = lesFraFil("snoedybder_vaer_en_stasjon_dogn.csv")
    plot_penvaersdager(datasett["snittSkydekke"])
    plot_temp_per_mnd(datasett["middeltemperatur"])
