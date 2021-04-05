from urllib.request import urlopen
import json
import configparser
from datetime import datetime

config = configparser.ConfigParser()
config.read('Settings.ini')
key = config["SETTINGS"]["key"]
quickfs_key = config["QUICKFS"]["key"]

def return_income(stock):
    url = "https://financialmodelingprep.com/api/v3/" + "income" + "-statement/" + stock + \
          "?limit=800&apikey=" + key
    response = urlopen(url)
    income = json.loads(response.read().decode("utf-8"))
    income.reverse()
    return income


def return_balance_sheet(stock):
    url = "https://financialmodelingprep.com/api/v3/" + "balance-sheet" + "-statement/" + stock + \
          "?limit=800&apikey=" + key
    response = urlopen(url)
    balance = json.loads(response.read().decode("utf-8"))
    balance.reverse()
    return balance


def return_cash_flow(stock):
    url = "https://financialmodelingprep.com/api/v3/" + "cash-flow" + "-statement/" + stock + \
          "?limit=800&apikey=" + key
    response = urlopen(url)
    cash = json.loads(response.read().decode("utf-8"))
    cash.reverse()
    return cash


def return_stock_quote(stock):
    url = "https://financialmodelingprep.com/api/v3/" + "quote/" + stock + "?apikey=" + key
    response = urlopen(url)
    return json.loads(response.read().decode("utf-8"))[0]


def return_stock_profile(stock):
    url = "https://financialmodelingprep.com/api/v3/" + "profile/" + stock + "?apikey=" + key
    response = urlopen(url)
    return json.loads(response.read().decode("utf-8"))[0]


def return_processed_data(income, balance, cash, profile):
    # data for output
    dates = []
    free_cash_flow = []
    net_income = []
    revenue = []
    current_equity = []
    stockholder_equity = []
    total_debt = []
    earnings_per_share = []
    dividends_paid = []

    print("cash")
    for year in cash:
        print(year)
        dates.append(datetime.strptime(year['date'], "%Y-%m-%d"))
        free_cash_flow.append(year['freeCashFlow'] / 1e6)
        dividends_paid.append(-year["dividendsPaid"] / 1e6)

    print("income")
    for year in income:
        print(year)
        net_income.append(year["netIncome"] / 1e6)
        revenue.append(year["revenue"] / 1e6)
        earnings_per_share.append(year["eps"])

    print("balance")
    for year in balance:
        print(year)
        current_equity.append(year["totalCurrentAssets"] / 1e6 - year["totalCurrentLiabilities"] / 1e6)
        stockholder_equity.append(year["totalStockholdersEquity"] / 1e6)
        total_debt.append(year["totalDebt"] / 1e6)

    print("profile")
    print(profile)
    # calculating derived ones
    return_on_equity = [100 * a / b if b != 0 else 0 for (a, b) in zip(net_income, stockholder_equity)]
    profit_margin = [100 * a / b if b != 0 else 0 for (a, b) in zip(net_income, revenue)]
    shares_outstanding = int(profile["mktCap"] / profile["price"])
    dividends_per_share = [x * 1e6 / shares_outstanding for x in dividends_paid]

    dates = dates[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    free_cash_flow = free_cash_flow[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    net_income = net_income[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    revenue = revenue[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    current_equity = current_equity[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    stockholder_equity = stockholder_equity[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    total_debt = total_debt[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    earnings_per_share = earnings_per_share[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    dividends_paid = dividends_paid[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    return_on_equity = return_on_equity[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    profit_margin = profit_margin[-min(len(free_cash_flow), len(revenue), len(total_debt)):]
    dividends_per_share = dividends_per_share[-min(len(free_cash_flow), len(revenue), len(total_debt)):]

    output_dictionary = {"Symbol": profile["symbol"],
                         "Dates": dates,
                         "FreeCashFlow": free_cash_flow,
                         "NetIncome": net_income,
                         "Revenue": revenue,
                         "CurrentEquity": current_equity,
                         "ShareholderEquity": stockholder_equity,
                         "Debt": total_debt,
                         "EPS": earnings_per_share,
                         "Dividends": dividends_paid,
                         "ROE": return_on_equity,
                         "ProfitMargin": profit_margin,
                         "DividendsPerShare": dividends_per_share}
    return output_dictionary


def return_processed_data_quickfs(stock):
    url = "https://public-api.quickfs.net/v1/data/all-data/"+stock+":US?api_key=" + quickfs_key
    response = urlopen(url)
    received_data = json.loads(response.read().decode("utf-8"))

    annual_data = received_data["data"]["financials"]["annual"]
    metadata = received_data["data"]["metadata"]

    dates = annual_data["period_end_date"]
    revenue = [x*1e-6 for x in annual_data["revenue"]]
    net_income = [x*1e-6 for x in annual_data["net_income"]]
    dividends_per_share = annual_data["dividends"]
    stockholder_equity = [x*1e-6 for x in annual_data["total_equity"]]
    free_cash_flow = [x*1e-6 for x in annual_data["fcf"]]
    total_debt = [x*1e-6 for x in annual_data["net_debt"]]
    current_equity = [(a-b)*1e-6 for (a, b) in zip(annual_data["total_current_assets"],
                                                   annual_data["total_current_liabilities"])]
    earnings_per_share = annual_data["eps_basic"]
    return_on_equity = [x*100 for x in annual_data["roe"]]
    # roic = [x*100 for x in annual_data["roic"]]
    profit_margin = [x*100 for x in annual_data["net_income_margin"]]

    output_dictionary = {"Symbol": metadata["symbol"],
                         "Dates": dates,
                         "FreeCashFlow": free_cash_flow,
                         "NetIncome": net_income,
                         "Revenue": revenue,
                         "CurrentEquity": current_equity,
                         "ShareholderEquity": stockholder_equity,
                         "Debt": total_debt,
                         "EPS": earnings_per_share,
                         "ROE": return_on_equity,
                         "ProfitMargin": profit_margin,
                         "DividendsPerShare": dividends_per_share}
    return output_dictionary
