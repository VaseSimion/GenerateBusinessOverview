import DatabaseStocks as Ds
import finviz


for stock in Ds.get_investing_lists():
    try:
        data = finviz.get_stock(stock)
        if float(data["P/S"]) < 1:
            if float(data["P/E"]) < 40:
                print(stock, "\nP/S:", data["P/S"], "\nP/E:", data["P/E"])
    except:
        pass

