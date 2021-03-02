import ExtractData as Ed

stock = "CVS"
balance = Ed.return_balance_sheet(stock)
income = Ed.return_income(stock)
cash = Ed.return_cash_flow(stock)

for line in cash:
    print(line)