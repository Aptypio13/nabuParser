import datetime
import sys

import matplotlib

from nabu.model.Currency import Currency

matplotlib.use("agg")
import matplotlib.pyplot as plt


def main () -> None :
    print("Hello world")


def pringChart(currencys: list[Currency]):
    dates: list[str] = []
    rates: list[float] = []

    for value in currencys:
        dates.append(str(value.date))

    for value in currencys:
        rates.append(value.rate)

    plt.figure(figsize=(dates.__len__(), rates.__len__() / 5))
    plt.plot(dates, rates, color="green", label=f"{currencys[0].name} for {dates[0]} - {dates[dates.__len__() - 1]}")
    plt.xlabel("Date")
    plt.yscale("linear")
    plt.tick_params(axis='x', labelsize=8) # set a font size for x
    plt.grid(True)
    plt.savefig(f"{datetime.date.today()}")


def testing_run():
    x = [-20, -15, 10, 0, 10, 15, 20]
    y = [-20, -15, -30, 0, 10, 15, 20]
    plt.plot(x, y)
    plt.savefig("test_figure.png", format = "png")
    print("testing")


if __name__ == '__main__':
    sys.exit(main())