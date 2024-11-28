import json

from binance.spot import Spot

# with open('../configs/config.json', 'r') as json_file:

def create(config_path: str,) -> Spot :
    with open(config_path, 'r') as json_file:
        config_data = json.load(json_file)

    api: str = config_data["binance"]["api"]
    secret: str = config_data["binance"]["secret"]
    return Spot(api_key=api, api_secret=secret)

def getSpotAccount(spotClient: Spot, only_non_ziro : bool = False, timeout : int = 1000) -> str :
    print(spotClient.ticker_price(symbol="BTCUSDT"))
    params = {
        'omitZeroBalances': str(only_non_ziro),
        'recvWindow' : timeout
    }
    print(spotClient.account(**params))
    return "good"

def getAccountBalance(spotClient: Spot) -> str :
    return spotClient.balance()


def getAllAccountOrders(spotClient: Spot) -> str :
    return spotClient.get_orders()


def getOrderByID(spotClient: Spot, id: int) -> str :
    params = {
        'orderId' : id
    }
    return spotClient.get_orders(params)

print(getSpotAccount(create('../../configs/config.json')))