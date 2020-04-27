from functions import isCountry, getCountry, getCountryStatistic, getAllStatistic, dotEveryThreeNumber, bubble_sort1, sortData
from getData import getData

covidData = sortData(getData("/country/all?format=json"))
covidTotalData = getData("/totals?format=json")
covidAllCountries = getData("/help/countries?format=json")


def location(country):
    if isCountry(country, covidData):
        return getCountryStatistic(getCountry(country, covidData))
    else:
        return getAllStatistic(covidTotalData[0])


def getAllCountries():
    space = "     "
    text = " "
    for data in covidData:
        text += str(data['country']) + space + "😷" + dotEveryThreeNumber(str(data['confirmed'])) + space + "💀" + \
            dotEveryThreeNumber(str(data['deaths'])) + space + "👍" + \
            dotEveryThreeNumber(str(data['recovered'])) + "\n\n"
    text += "\nСтрана  😷 Заболевших  💀 Смертей   👍 Выздоровевших  "
    return text


def getTopNumber(word):
    text = " "
    space = "     "
    word = int(word.split("-")[1])
    for i in range(len(covidData)-word, len(covidData), 1):
        data = covidData[i]
        print(data)
        text += str(data['country']) + space + "😷" + dotEveryThreeNumber(str(data['confirmed'])) + space + "💀" + \
            dotEveryThreeNumber(str(data['deaths'])) + space + "👍" + \
            dotEveryThreeNumber(str(data['recovered'])) + "\n\n"
    text += "\nСтрана  😷 Заболевших  💀 Смертей   👍 Выздоровевших:  "
    return text
