import json
from datetime import datetime

import requests

from nabu.chart.chartPrinter import createChart
from nabu.model.Currency import Currency
from nabu.utils.Parsers import jsonToCurrency
from nabu.utils.Parsers import parseDate


#get valcode for currency, valcode is essential for request
def getValcode(data: json, currency: str) -> str:
    try:
        return data["valcode"][f"{currency}"]
    except:
        print(f"Currency with name {currency} not found")
        return ""

#printing course for range
def printRangeCurse(currency: str, dateFrom: datetime.date, dateTo: datetime.date) -> None :
    with open('configs/config.json', 'r') as json_file:
        config_data = json.load(json_file)

    naby_url: str = config_data["url"]["range"]
    valcode: str = getValcode(config_data, currency)
    response = requests.get(naby_url + f"?start={parseDate(dateFrom)}&end={parseDate(dateTo)}&valcode={valcode}&sort=exchangedate&order=desc&json")

    if response.status_code == 200:
     body = response.json()
     currencys: list[Currency] = jsonToCurrency(body)
     createChart(currencys)
     for value in currencys:
         print(value.__str__())
    else:
     print("Error:", response.status_code)



def printCurrentCurse(currency: str) -> None :
    with open('/configs/config.json', 'r') as json_file:
        config_data = json.load(json_file)

    naby_url: str = config_data["url"]["nabu"]
    valcode: str = getValcode(config_data, currency)

    response = requests.get(naby_url + f"?valcode={valcode}&json")

    if response.status_code == 200:
        body = response.json()
        currency = jsonToCurrency(body)
        print(Currency.__str__(currency[0]))
    else:
        print("Error:", response.status_code)

#get current curse for currency by name
def getCurrentCurse(currency: str) -> Currency :
    with open('configs/config.json', 'r') as json_file:
        config_data = json.load(json_file)

    naby_url: str = config_data["url"]["nabu"]
    valcode: str = getValcode(config_data, currency)

    response = requests.get(naby_url + f"?valcode={valcode}&json")

    if response.status_code == 200:
        body = response.json()
        currency = jsonToCurrency(body)
        return currency[0]
    else:
        print("Error:", response.status_code)

