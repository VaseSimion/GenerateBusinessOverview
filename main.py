import ExtractData as Ed
import GraphFunctions as Gf
import Report as Rp
import DatabaseStocks as Ds

using_financial_prep = True
stock = Ds.get_random_stock()

if using_financial_prep:
    stock = "MSFT"
    balance = Ed.return_balance_sheet(stock)
    income = Ed.return_income(stock)
    cash = Ed.return_cash_flow(stock)
    profile = Ed.return_stock_profile(stock)
    processed_data = Ed.return_processed_data(income, balance, cash, profile)
else:
    stock = "AAWW"
    profile = Ed.return_stock_profile(stock)
    processed_data = Ed.return_processed_data_quickfs(stock)

#TODO: Text for description
#TODO: colors
#TODO: Graph description
#TODO: References

Gf.save_all_support_file(processed_data)

Rp.write_the_report(processed_data, profile)
