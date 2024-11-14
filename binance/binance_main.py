import json
import logging
import requests
from binance.spot import Spot
import time
import win32api
from win32api import SetSystemTime, GetSystemTime


def getSpotAccount() -> str :
    print("starting")
    with open('../configs/config.json', 'r') as json_file:
        config_data = json.load(json_file)

    client = Spot()
    print(f"time: {client.time()}")
    api: str = config_data["binance"]["api"]
    secret: str = config_data["binance"]["secret"]
    spotClient = Spot(api_key=api, api_secret=secret)
    print(GetSystemTime())
    print(spotClient.time())
    print(spotClient.account())
    return "good"

print(getSpotAccount())