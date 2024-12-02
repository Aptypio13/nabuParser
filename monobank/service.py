import datetime
import json

import requests


def getCurrencys():
    with open('configs/config.json', 'r') as json_file:
        config_data = json.load(json_file)
    url: str = config_data["url"]["monobank"]
    codes: dict[str, str] = config_data["iso-4217"]
    responce = requests.get(url)
    if responce.status_code == 200 :
        responceJson = responce.json()
        for v in responceJson:
            currencyFrom = isoToCode(str(v["currencyCodeA"]), codes)
            currencyTo = isoToCode(str(v["currencyCodeB"]), codes)
            date = datetime.date.fromtimestamp(v["date"])
            try :
                rateBuy = v["rateBuy"]
            except:
                rateBuy = 0.0
            try :
                rateSell = v["rateSell"]
            except:
                rateSell = 0.0

            try :
                rateCross = v["rateCross"]
            except:
                rateCross = 0.0

            print(f" At {date} from {currencyFrom} to {currencyTo} buy price = {rateBuy} and sell price = {rateSell}, rateCross = {rateCross}")
        return responceJson
    else:
        return f"Error: {responce.status_code} + {responce.text}"


def isoToCode(iso: str, codesDictionary: dict[str, str]) -> str:
    try:
        return codesDictionary.get(iso)
    except:
        print(f"Can't find {iso} in base")
        return iso