import math


def isCountry(country, data):
    for item in data:
        if item['country'] == country:
            return True


def getCountry(country, data):
    for item in data:
        if item['country'] == country:
            return item


def getCountryStatistic(country):
    name = str(country['country'])
    confirmed = dotEveryThreeNumber(str(country['confirmed']))
    deaths = dotEveryThreeNumber(str(country['deaths']))
    recovered = dotEveryThreeNumber(str(country['recovered']))
    text = "Страна: {} \nЗаболевших: {} \nСметрей: {} \nВыздоровел: {}".format(name,
                                                                               confirmed, deaths, recovered)
    return text


def getAllStatistic(data):
    confirmed = dotEveryThreeNumber(str(data['confirmed']))
    deaths = dotEveryThreeNumber(str(data['deaths']))
    recovered = dotEveryThreeNumber(str(data['recovered']))
    text = "Данные по всему миру: \nЗаболевших: {} \nСметрей: {} \nВыздоровел: {}".format(confirmed, deaths, recovered)
    return text


def dotEveryThreeNumber(number):
    strNumber = str(number)
    splitNumber = list(strNumber)
    lenNumber = len(strNumber)
    i = lenNumber - 1
    while i > 0:
        if(i == lenNumber - 3 or i == lenNumber - 6 or i == lenNumber - 9):
            splitNumber.insert(i, ".")
        i -= 1
    number = "".join(splitNumber)
    return number
