import json
from datetime import datetime

from nabu.model import Currency

def jsonToCurrency(body: json) -> list[Currency] :
    result: list[Currency] = []
    try:
        for item in body:
            id = item["r030"]
            name = item["txt"]
            rate = item["rate"]
            cc = item["cc"]
            date = item["exchangedate"]
            result.append(Currency.Currency(id, cc, name, rate, date))
        return result
    except:
        print(f"Error: {body}")
        return list[Currency]()

def isoToCode(iso_code: int) -> str:
    with open('configs/config.json', 'r') as json_file:
        config_data = json.load(json_file)
    codes: dict[str] = config_data["iso-4217"]
    try:
       return codes.get(str(iso_code))
    except:
        print("ISO-Code invalid")
        return "None"

def parseDate(date: datetime.date) -> str :
    return str(date).replace(".", "").replace("-", "").replace("/", "")