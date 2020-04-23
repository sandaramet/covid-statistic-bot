from functions import isCountry, getCountry, getStatistic
from getData import getData

covidData = getData("/country/all?format=json")
covidTotalData = getData("/totals?format=json")
covidAllCountries = getData("/help/countries?format=json")


def location(country):
    isCountry(country, covidData)

    if isCountry(country, covidData):
        return getStatistic(getCountry(country, covidData))
    else:
        return getStatistic(covidTotalData[0])

def getAllCountries():
    text = " "
    for country in covidAllCountries:
        text += country['name'] + "\n"
    return text

