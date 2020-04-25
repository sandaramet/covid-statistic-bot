from functions import isCountry, getCountry, getCountryStatistic, getAllStatistic, dotEveryThreeNumber
from getData import getData

covidData = getData("/country/all?format=json")
covidTotalData = getData("/totals?format=json")
covidAllCountries = getData("/help/countries?format=json")


def location(country):
    if isCountry(country, covidData):
        return getCountryStatistic(getCountry(country, covidData))
    else:
        return getAllStatistic(covidTotalData[0])


def getAllCountries():
    print(covidData)
    space = "     "
    text = "Страна  😷 Заболевших  💀 Сметрей   👍 Выздоровел  \n"
    for data in covidData:
        text += str(data['country']) + space + "😷" + dotEveryThreeNumber(str(data['confirmed'])) + space + "💀" + \
            dotEveryThreeNumber(str(data['deaths'])) + space + "👍" + \
            dotEveryThreeNumber(str(data['recovered'])) + "\n\n"
    return text
