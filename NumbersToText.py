import numpy as np


def free_cash_flow_analysis(data):
    list_to_interpret = data["FreeCashFlow"]
    if len(list_to_interpret) < 2:
        return ["Not enough financial data to conclude anything", 0]
    if list_to_interpret[-1] > list_to_interpret[-2]:
        if len(list_to_interpret) > 2 and list_to_interpret[-2] > list_to_interpret[-3]:
            if len(list_to_interpret) > 3 and list_to_interpret[-3] > list_to_interpret[-4]:
                if len(list_to_interpret) > 4 and list_to_interpret[-4] > list_to_interpret[-5]:
                    return ["The free cash flow has been increasing every year in the last 4 years.", 4]
                else:
                    return ["The free cash flow has been increasing every year in the last 3 years.", 3]
            else:
                return ["The free cash flow has been increasing every year in the last 2 years.", 2]
        else:
            return ["The free cash flow has been increasing in the last year.", 1]
    else:
        return ["The free cash flow decreased in the last year.", 0]


def revenue_analysis(data):
    list_to_interpret = data["Revenue"]
    if len(list_to_interpret) < 2:
        return ["Not enough financial data to conclude anything", 0]
    if list_to_interpret[-1] > list_to_interpret[-2]:
        if len(list_to_interpret) > 2 and list_to_interpret[-2] > list_to_interpret[-3]:
            if len(list_to_interpret) > 3 and list_to_interpret[-3] > list_to_interpret[-4]:
                if len(list_to_interpret) > 4 and list_to_interpret[-4] > list_to_interpret[-5]:
                    return ["The revenue has been increasing every year in the last 4 years.", 4]
                else:
                    return ["The revenue has been increasing every year in the last 3 years.", 3]
            else:
                return ["The revenue has been increasing every year in the last 2 years.", 2]
        else:
            return ["The revenue has been increasing in the last year.", 1]
    else:
        return ["The revenue decreased in the last year.", 0]


def net_income_analysis(data):
    list_to_interpret = data["NetIncome"]
    if len(list_to_interpret) < 2:
        return ["Not enough financial data to conclude anything", 0]
    if list_to_interpret[-1] > list_to_interpret[-2]:
        if len(list_to_interpret) > 2 and list_to_interpret[-2] > list_to_interpret[-3]:
            if len(list_to_interpret) > 3 and list_to_interpret[-3] > list_to_interpret[-4]:
                if len(list_to_interpret) > 4 and list_to_interpret[-4] > list_to_interpret[-5]:
                    return ["The net income has been increasing every year in the last 4 years.", 4]
                else:
                    return ["The net income has been increasing every year in the last 3 years.", 3]
            else:
                return ["The net income has been increasing every year in the last 2 years.", 2]
        else:
            return ["The net income has been increasing in the last year.", 1]
    else:
        return ["The net income decreased in the last year.", 0]


def profit_margin_analysis(data):
    list_to_interpret = data["ProfitMargin"]
    if len(list_to_interpret) < 2:
        return ["Not enough financial data to conclude anything", 0]
    if list_to_interpret[-1] > list_to_interpret[-2]:
        if len(list_to_interpret) > 2 and list_to_interpret[-2] > list_to_interpret[-3]:
            if len(list_to_interpret) > 3 and list_to_interpret[-3] > list_to_interpret[-4]:
                if len(list_to_interpret) > 4 and list_to_interpret[-4] > list_to_interpret[-5]:
                    return ["The profit margin has been increasing every year in the last 4 years.", 4]
                else:
                    return ["The profit margin has been increasing every year in the last 3 years.", 3]
            else:
                return ["The profit margin has been increasing every year in the last 2 years.", 2]
        else:
            return ["The profit margin has been increasing in the last year.", 1]
    else:
        return ["The profit margin decreased in the last year.", 0]


def roe_analysis(data):
    list_to_interpret = data["ROE"]
    if len(list_to_interpret) < 2:
        return ["Not enough financial data to conclude anything", 0]
    if list_to_interpret[-1] > list_to_interpret[-2]:
        if len(list_to_interpret) > 2 and list_to_interpret[-2] > list_to_interpret[-3]:
            if len(list_to_interpret) > 3 and list_to_interpret[-3] > list_to_interpret[-4]:
                if len(list_to_interpret) > 4 and list_to_interpret[-4] > list_to_interpret[-5]:
                    return ["The return on equity has been increasing every year in the last 4 years.", 4]
                else:
                    return ["The return on equity has been increasing every year in the last 3 years.", 3]
            else:
                return ["The return on equity has been increasing every year in the last 2 years.", 2]
        else:
            return ["The return on equity has been increasing in the last year.", 1]
    else:
        return ["The return on equity decreased in the last year.", 0]


def simple_free_cash_flow_prediction(data):
    fcf = data["FreeCashFlow"][-1] * 1e-3
    summed = 0
    for i in range(10):
        #print(i, fcf)
        summed += fcf
        if i == 9:
            #print(i, 10 * fcf)
            summed += 10 * fcf
        fcf = fcf * 0.9
    summed = round(summed, 2)
    return "According to a simple fcf analysis the intrinsec value discounted with 10% per year is {} billions".\
        format(summed)


def extrapolated_free_cash_flow_prediction(data):
    y = [fcf * 1e-3 for fcf in data["FreeCashFlow"][-5:]]
    x = [1, 2, 3, 4, 5]
    x = x[:len(y)]
    predictions = [max(x) + y for y in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    #print(x, y)
    print(np.polyfit(x, y, 1))
    f = np.poly1d(np.polyfit(x, y, 1))

    future_fcf = f(predictions)
    #print(future_fcf)
    summed = 0
    for index, value in enumerate(future_fcf):
        summed += value * 0.9 ** (index+1)
        #print(value, value * 0.9 ** (index+1))
        if index == 9:
            summed += 10 * value * 0.9 ** (index+1)

    summed = round(summed, 2)
    return "According to a extrapolated fcf analysis the intrinsec value discounted with 10% per year is {} billions".\
        format(summed)


def calculated_sticker_price_according_to_rule_1_book(data):
    if data["5yAverage"][1] == "NA":  # [avg10y_roic, avg10y_equity, avg10y_eps, avg10y_fcf]
        return "According to rule 1 investing book, the fundamentals are not good enough to invest in this"
    if data["10yAverage"][1] != "NA":
        earnings_rate = max(data["10yAverage"][1], data["5yAverage"][1])  # in the book the equity grwth is used as future EPS growth
    else:
        earnings_rate = data["5yAverage"][1]  # in the book the equity grwth is used as future EPS growth
    print("earnings growth rate is ", earnings_rate)
    if earnings_rate < 7 or data["5yAverage"][0] < 7:
        return "According to rule 1 investing book, the fundamentals are not good enough to invest in this"

    eps = data["EPS"][-1]
    print("EPS is ", eps)
    future_eps = eps * ((1 + earnings_rate/100)**10)
    print("future EPS is ",future_eps)
    future_price = min(2*earnings_rate, data["MedianPE"]) * future_eps
    print("MEdian pe is",  data["MedianPE"])
    print("future price is ", future_price)
    reduced_price_to_now = round((future_price / 4.04), 2)
    return "According to rule 1 investing book, the price now to cover 15% increase without margin of safety is " + \
           str(reduced_price_to_now)