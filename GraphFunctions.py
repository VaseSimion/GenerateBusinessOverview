import numpy as np
import tulipy as ti
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import yfinance as yf
from datetime import  datetime

def save_macd_buy(stock_name):
    stock = yf.download(tickers=stock_name, interval="1d", period="2y", threads=True)
    closing_price_list = stock['Close'].tolist()
    date_list = list(stock.index)

    numpyclose = np.asarray(closing_price_list)
    macd1, macd2, macdhistogram = ti.macd(numpyclose, 8, 17, 9)  # for buy signals it should be 8,17,9
    sma = ti.sma(numpyclose, 17)

    plt.figure(figsize=(15, 8))
    ax1 = plt.subplot(212)
    ax2 = plt.subplot(211, sharex=ax1, title=stock_name)
    numberofactivedays = len(date_list[16:])
    arrangeddates = np.arange(numberofactivedays)
    ax1.plot(arrangeddates, macd1, 'r')
    ax1.plot(arrangeddates, macd2, 'y')
    ax1.bar(arrangeddates, macdhistogram)
    ax1.plot(arrangeddates, [0] * len(date_list[16:]))
    ax1.set(ylabel='MACD')
    ax2.plot(arrangeddates, closing_price_list[16:])
    ax2.plot(arrangeddates, sma, 'r')
    ax2.set(ylabel="Price")

    ax1.set_xticks(np.append(arrangeddates[0::60], arrangeddates[-1]))
    ax2.set_xticks(np.append(arrangeddates[0::60], arrangeddates[-1]))
    ax1.set_xticklabels([date.strftime("%Y-%m-%d") for date in date_list[16:]][0::60] +
                        [[date.strftime("%Y-%m-%d") for date in date_list[16:]][-1]])
    ax2.set_xticklabels([date.strftime("%Y-%m-%d") for date in date_list[16:]][0::60] +
                        [[date.strftime("%Y-%m-%d") for date in date_list[16:]][-1]])
    ax1.tick_params(rotation=30)
    ax2.tick_params(rotation=30)
    plt.savefig("Support Files/" + stock_name + "-price" + ".png")
    plt.close()


def save_free_cash_flow(cash_flow):
    dates = []
    free_cash_flow = []
    for year in cash_flow:
        dates.append(datetime.strptime(year['date'], "%Y-%m-%d"))
        free_cash_flow.append(year['freeCashFlow'] / 1e6)
    plt.figure(figsize=(15, 8))
    plt.plot(dates, free_cash_flow)
    plt.legend(["free cash flow"])
    plt.savefig("Support Files/freecash_flow.png")
    plt.close()

