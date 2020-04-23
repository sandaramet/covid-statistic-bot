
def isCountry(country, data):
    for item in data:
        if item['country'] == country:
            return True
            break


def getCountry(country, data):
    for item in data:
        if item['country'] == country:
            return item
            break


def getStatistic(country):
    confirmed = str(country['confirmed'])
    deaths = str(country['deaths'])
    recovered = str(country['recovered'])
    text = "Заболевших: {} \nСметрей: {} \nВыздоровел: {}".format(
        confirmed, deaths, recovered)
    return text



