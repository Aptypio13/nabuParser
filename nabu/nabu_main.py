from datetime import datetime
from locale import currency

import requests
import json

from nabu.model.Currency import Currency

with open('../configs/config.json', 'r') as json_file:
    config_data = json.load(json_file)


naby_url: str = config_data["url"]["nabu"]
euro_valcode: str = config_data["valcode"]["euro"]

response = requests.get(naby_url+f"?valcode={euro_valcode}&json")

def jsonToCurrency(body: json) -> Currency :
    for item in body:
        id = item["r030"]
        name = item["txt"]
        rate = item["rate"]
        cc = item["cc"]
        date = item["exchangedate"]
        return Currency(id, cc, name, rate, date)

if response.status_code == 200:
    body = response.json()
    currency = jsonToCurrency(body)
    print(Currency.__str__(currency))
else:
    print("Error:", response.status_code)

