from functions import isCountry, getCountry, getCountryStatistic, getAllStatistic, dotEveryThreeNumber, bubble_sort1
from getData import getData

covidData = getData("/country/all?format=json")
covidTotalData = getData("/totals?format=json")
covidAllCountries = getData("/help/countries?format=json")


def location(country):
    if isCountry(country, covidData):
        return getCountryStatistic(getCountry(country, covidData))
    else:
        return getAllStatistic(covidTotalData[0])


# def sort(nums):
#     for i in range(len(nums) - 1, 0, -1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp


def sortData(data):
    
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j]['confirmed'] > data[j+1]['confirmed']:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp


sortData(covidData)
# for i in covidData:
#     print(i['confirmed'])
# print(covidData)


def getAllCountries():
    space = "     "
    text = " "
    for data in covidData:
        text += str(data['country']) + space + "😷" + dotEveryThreeNumber(str(data['confirmed'])) + space + "💀" + \
            dotEveryThreeNumber(str(data['deaths'])) + space + "👍" + \
            dotEveryThreeNumber(str(data['recovered'])) + "\n\n"
    text += "\nСтрана  😷 Заболевших  💀 Сметрей   👍 Выздоровел  "
    return text
