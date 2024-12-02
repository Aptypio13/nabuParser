import pandas as pd
from filetype import match
from pandas import DataFrame

from nabu.model.Currency import Currency


def currencysToDataFrame(currencys: list[Currency]) -> DataFrame :
    dates = []
    rates = []
    for currency in currencys :
        dates.append(currency.date)
        rates.append(currency.rate)
    dates.reverse()
    rates.reverse()
    return pd.DataFrame({"Date": dates, "rates": rates})


def createExel(currencys: list[Currency], name: str = None):
   frame = currencysToDataFrame(currencys)
   try:
       match name:
           case None: frame.to_excel("currencys.xlsx")
           case _ : frame.to_excel(f"{name}.xlsx")
   except :
       print(f"Error occurred while creating excel")


