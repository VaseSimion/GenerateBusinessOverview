from urllib.request import urlopen
import json
import configparser

config = configparser.ConfigParser()
config.read('Settings.ini')
key = config["SETTINGS"]["key"]


def return_income(stock):
    url = "https://financialmodelingprep.com/api/v3/" + "income" + "-statement/" + stock + \
          "?limit=800&apikey=" + key
    response = urlopen(url)
    income = json.loads(response.read().decode("utf-8"))
    return income

def return_balance_sheet(stock):
    url = "https://financialmodelingprep.com/api/v3/" + "balance-sheet" + "-statement/" + stock + \
          "?limit=800&apikey=" + key
    response = urlopen(url)
    balance = json.loads(response.read().decode("utf-8"))
    return balance

def return_cash_flow(stock):
    url = "https://financialmodelingprep.com/api/v3/" + "cash-flow" + "-statement/" + stock + \
          "?limit=800&apikey=" + key
    response = urlopen(url)
    cash = json.loads(response.read().decode("utf-8"))
    return cash
