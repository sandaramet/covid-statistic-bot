import http.client
import json
conn = http.client.HTTPSConnection(
    "covid-19-data.p.rapidapi.com")  # api server
headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "4fdf5e2690msh6710b6eacf0db0dp119dcfjsnb978114cc784"
}


def getData(url="/country/all?format=json"):
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    countriesData = json.loads(data.decode("utf-8"))
    return countriesData

