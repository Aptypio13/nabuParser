from typing import Union

from pydantic import BaseModel

from nabu.model.Currency import Currency
from nabu.nabu_main import getCurrentCurse
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.put("/currency/{valcode}&{valcodeTo}/{amount}")
def get_currency_to_currency(valcode: str, valcodeTo: str, amount: float):
    print(f"Calculating {amount} {valcode} to {valcodeTo}")
    currencyCourseFrom = getCurrentCurse(valcode)
    currencyCourseTo = getCurrentCurse(valcodeTo)
    result = (amount * currencyCourseFrom.rate) / currencyCourseTo.rate
    return {f"on {currencyCourseTo.date} {amount} {valcode} to {valcodeTo} = {result}"}

@app.get("/currencyy/{valcode}")
def get_currency(valcode: str):
    amount = 150
    print(f"Calculating {amount} currency for {valcode}")
    currentCourse: Currency = getCurrentCurse("euro")
    result = amount / currentCourse.rate
    print({f"{amount}грн в {valcode}" : result})
    return {"result": result}


@app.get("/hello/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

