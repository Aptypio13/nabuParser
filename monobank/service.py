import json
import requests


def getCurrencys():
    with open('configs/config.json', 'r') as json_file:
        config_data = json.load(json_file)
    url: str = config_data["url"]["monobank"]
    responce = requests.get(url)
    if responce.status_code == 200 :
        responceJson = responce.json()
        for v in responceJson:
            currencyFrom = v["currencyCodeA"]
            currencyTo = v["currencyCodeB"]
            date = v["date"]
            # rateBuy: float = v["rateBuy"]
            # rateSell: float = v["rateSell"]
            print(f" At {date} from {currencyFrom} to {currencyTo} buy price = 0 and sell price = {10}")
        return responceJson
    else:
        return f"Error: {responce.status_code} + {responce.text}"