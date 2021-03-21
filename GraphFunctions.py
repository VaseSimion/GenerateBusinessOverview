import numpy as np
import tulipy as ti
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import yfinance as yf
from datetime import datetime, timedelta
import math


def save_macd_buy(stock_name):
    stock = yf.download(tickers=stock_name, interval="1wk", period="2y", threads=True)
    stock.index = stock.index.where(~stock.index.duplicated(), stock.index + timedelta(1))
    # Remove all the NaN values
    for index, row in stock.iterrows():
        if math.isnan(row["Close"]) or math.isnan(row["Volume"]):
            stock = stock.drop([index])
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

    ax1.set_xticks(np.append(arrangeddates[0::15], arrangeddates[-1]))
    ax2.set_xticks(np.append(arrangeddates[0::15], arrangeddates[-1]))
    ax1.set_xticklabels([date.strftime("%Y-%m-%d") for date in date_list[16:]][0::15] +
                        [[date.strftime("%Y-%m-%d") for date in date_list[16:]][-1]])
    ax2.set_xticklabels([date.strftime("%Y-%m-%d") for date in date_list[16:]][0::15] +
                        [[date.strftime("%Y-%m-%d") for date in date_list[16:]][-1]])
    ax1.tick_params(rotation=30)
    ax2.tick_params(rotation=30)
    plt.savefig("Support Files/" + stock_name + "-price" + ".png")
    plt.close()


def save_generic_millions(dates, data_to_plot, stock_name, data_name, units):
    fig = plt.figure(figsize=(15, 4))
    ax = fig.add_subplot(111)
    plt.plot(dates, data_to_plot)
    for i, j in zip(dates, data_to_plot):
        ax.annotate(str(j), xy=(i, round(j, 2)))
    increase = [0]
    for index, value in enumerate(data_to_plot):
        if index > 0:
            increase.append(value-data_to_plot[index-1])
    plt.bar(dates[1:], increase[1:], width=100)
    plt.legend([data_name, "Increase in " + data_name.lower()])
    plt.xlabel("Time")
    plt.ylabel(data_name + " " + units)
    plt.savefig("Support Files/" + stock_name + data_name + ".png")
    plt.close()


def save_two_generic_millions(dates, data_to_plot, data_to_plot_2, stock_name, data_name, data_name_2, units):
    plt.figure(figsize=(15, 4))
    plt.plot(dates, data_to_plot)
    plt.plot(dates, data_to_plot_2)
    plt.legend([data_name, data_name_2])
    plt.xlabel("Time")
    plt.ylabel(data_name + " and " + data_name_2 + " "+ units)
    plt.savefig("Support Files/" + stock_name + data_name + data_name_2 + ".png")
    plt.close()


def save_all_support_file(processed_data):
    save_macd_buy(processed_data["Symbol"])
    save_generic_millions(processed_data["Dates"], processed_data["FreeCashFlow"], processed_data["Symbol"],
                             "Free cash flow", "[mil $]")
    save_generic_millions(processed_data["Dates"], processed_data["NetIncome"], processed_data["Symbol"],
                             "Net income", "[mil $]")
    save_generic_millions(processed_data["Dates"], processed_data["Revenue"], processed_data["Symbol"],
                             "Revenue", "[mil $]")
    save_generic_millions(processed_data["Dates"], processed_data["EPS"], processed_data["Symbol"],
                             "Earnings per share", "[$]")
    save_generic_millions(processed_data["Dates"], processed_data["DividendsPerShare"], processed_data["Symbol"],
                             "Dividends per share", "[$]*")
    save_generic_millions(processed_data["Dates"], processed_data["Dividends"], processed_data["Symbol"],
                             "Dividends paid", "[mil $]")
    save_generic_millions(processed_data["Dates"], processed_data["ROE"], processed_data["Symbol"],
                             "Return on equity", "[%]")
    save_generic_millions(processed_data["Dates"], processed_data["ProfitMargin"], processed_data["Symbol"],
                             "Profit margin", "[%]")
    save_two_generic_millions(processed_data["Dates"], processed_data["CurrentEquity"],
                                 processed_data["ShareholderEquity"],
                                 processed_data["Symbol"], "Current Equity", "Shareholder Equity", "[mil $]")
    save_two_generic_millions(processed_data["Dates"], processed_data["CurrentEquity"],
                                 processed_data["ShareholderEquity"],
                                 processed_data["Symbol"], "Current Equity", "Shareholder Equity", "[mil $]")
    save_two_generic_millions(processed_data["Dates"], processed_data["Debt"], processed_data["ShareholderEquity"],
                                 processed_data["Symbol"], "Debt", "Shareholder Equity", "[mil $]")

    #TODO: Add free cash flow and net income in the same graph: https://www.investopedia.com/terms/f/freecashflow.asp