from datetime import datetime

import requests
import json
from nabu.utils.Parsers import jsonToCurrency
from nabu.utils.Parsers import parseDate
from nabu.chart.chartPrinter import createChart

from nabu.model.Currency import Currency


def getValcode(data: json, currency: str) -> str:
    try:
        return data["valcode"][f"{currency}"]
    except:
        print(f"Currency with name {currency} not found")
        return ""

def printRangeCurse(currency: str, dateFrom: datetime.date, dateTo: datetime.date) -> None :
 # https://bank.gov.ua/NBU_Exchange/exchange_site?start=20220115&end=20220131&valcode=usd&sort=exchangedate&order=desc
    with open('../configs/config.json', 'r') as json_file:
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
    with open('../configs/config.json', 'r') as json_file:
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


d = printRangeCurse("euro", "2023.01.01", "2023.01.04")