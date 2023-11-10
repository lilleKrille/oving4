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


def plot_penvaersdager(datasett):
    snittskydekke = datasett["snittSkydekke"]
    data = dict()
    #obj is (VALUE, DATE)         obj[0] = VALUE, obj[1] = DATE
    for obj in snittskydekke:
        try:
            if obj[1].year in data:
                if float(obj[0]) <= 3:
                    data[obj[1].year] = data[obj[1].year] + 1
            else:
                if float(obj[0]) <= 3:
                    data[obj[1].year] = 0
        except ValueError:
            continue

    plt.plot(list(data.keys()), list(data.values()), "o-")
    plt.show()



if __name__ == "__main__":
    datasett = lesFraFil("snoedybder_vaer_en_stasjon_dogn.csv")
    plot_penvaersdager(datasett)