from datetime import datetime


class Currency :
    def __init__(self, id: int, code: str, name: str, rate: float, date: datetime.date):
        self.id = id
        self.code = code
        self.name = name
        self.rate = rate
        self.date = date

    def __str__(self):
        return f"Курс {self.name} на {self.date} = {self.rate}грн"


    def decode_currency(data):
        if "date" in data:
            data["date"] = datetime.datetime.strptime(data["date"], "%Y-%m-%d").date()
            return Currency(**data)
