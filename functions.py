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
    text = "Данные по всему миру: \nЗаболевших: {} \nСметрей: {} \nВыздоровел: {}".format(
        confirmed, deaths, recovered)
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


def bubble_sort1(A):
    for i in range(0, len(A) - 1):
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


def sortData(data):

    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j]['confirmed'] > data[j+1]['confirmed']:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    return data


def haveWord(eventText, word):
    eventText = eventText.split("-")[0]
    if(eventText == word):
        return True
    else:
        return False



