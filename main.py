import dateutil.parser as parser
from fastapi import FastAPI

from nabu.model.Currency import Currency
from nabu.nabu_main import *

app = FastAPI()


@app.get("/currency/{valcode}&{valcodeTo}/{amount}")
def get_currency_to_currency(valcode: str, valcodeTo: str, amount: float):
    print(f"Calculating {amount} {valcode} to {valcodeTo}")
    currencyCourseFrom = getCurrentCurse(valcode)
    currencyCourseTo = getCurrentCurse(valcodeTo)
    result = (amount * currencyCourseFrom.rate) / currencyCourseTo.rate
    return {f"On {currencyCourseTo.date} {amount} {valcode} to {valcodeTo} = {result}"}


@app.get("/currency/{valcode}")
def get_currency(valcode: str):
    currentCourse: Currency = getCurrentCurse(valcode)
    return {f"Current curse {valcode} to UAH": currentCourse.rate}


@app.get("/currency/range/{valcode}/{dateFrom}&{dateTo}")
def get_currency_range(valcode: str, dateFrom: str, dateTo: str):
    dateFrom = parser.parse(dateFrom)
    dateTo = parser.parse(dateTo)
    print(f"from = {dateFrom} \n to = {dateTo}")
    printRangeCurse(valcode, dateFrom.date(), dateTo.date())
    return ({"Range printed"})



@app.get("/print/range/{valcode}/{dateFrom}&{dateTo}")
def print_xmls_currency_range(valcode: str, dateFrom: str, dateTo: str):
    dateFrom = parser.parse(dateFrom)
    dateTo = parser.parse(dateTo)
    print(f"from = {dateFrom} \n to = {dateTo}")
    printCurrencysInXmls(valcode, dateFrom.date(), dateTo.date())
    return {"Range printed"}


@app.get("/mono")
def get_mono_currencies():
    import monobank.service as monobank_service
    print(monobank_service.getCurrencys())
    return {"DONE"}
