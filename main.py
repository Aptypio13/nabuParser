from datetime import datetime
from typing import Union

from pydantic import BaseModel

from nabu.model.Currency import Currency
from nabu.nabu_main import getCurrentCurse, printRangeCurse
from fastapi import FastAPI
import dateutil.parser as parser

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/currency/{valcode}&{valcodeTo}/{amount}")
def get_currency_to_currency(valcode: str, valcodeTo: str, amount: float):
    print(f"Calculating {amount} {valcode} to {valcodeTo}")
    currencyCourseFrom = getCurrentCurse(valcode)
    currencyCourseTo = getCurrentCurse(valcodeTo)
    print(
        f"from = {currencyCourseFrom}"
        f"to = {currencyCourseTo}"
    )
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
    return {"Range printed"}



@app.get("/hello/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

