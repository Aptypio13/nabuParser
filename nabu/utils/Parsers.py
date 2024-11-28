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


def parseDate(date: datetime.date) -> str :
    return str(date).replace(".", "").replace("-", "").replace("/", "")