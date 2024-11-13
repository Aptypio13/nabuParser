from quickchart import *
from nabu.model.Currency import Currency


def createChart(currencys: list[Currency]) -> None :
    dates: list[str] = []
    rates: list[float] = []

    for value in currencys :
        dates.append(value.date)

    for value in currencys :
        rates.append(value.rate)

    dates.reverse()
    qc = QuickChart()
    qc.width = 500
    qc.height = 300
    qc.config = {
        "type": "line",
        "data": {
            "labels": dates,
            "datasets": [{
                "label": f"{currencys[0].name.__str__()}",
                "data": rates,
                "fill": False,
                "borderColor": "green"
            }]
        }
    }

    print(qc.get_url())
    qc.to_file('C:/Users/Operator/PycharmProjects/pythonSandBox/nabu/mychart.png')
