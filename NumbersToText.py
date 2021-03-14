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


def dividends_analysis(data):
    list_to_interpret = data["Dividends"]
    if len(list_to_interpret) < 2:
        return ["Not enough financial data to conclude anything", 0]
    if list_to_interpret[-1] == 0:
        return ["This stock does not pay dividends", 0]
    if list_to_interpret[-1] > list_to_interpret[-2]:
        if len(list_to_interpret) > 2 and list_to_interpret[-2] > list_to_interpret[-3]:
            if len(list_to_interpret) > 3 and list_to_interpret[-3] > list_to_interpret[-4]:
                if len(list_to_interpret) > 4 and list_to_interpret[-4] > list_to_interpret[-5]:
                    return ["The dividends has been increasing every year in the last 4 years.", 4]
                else:
                    return ["The dividends has been increasing every year in the last 3 years.", 3]
            else:
                return ["The dividends has been increasing every year in the last 2 years.", 2]
        else:
            return ["The dividends has been increasing in the last year.", 1]
    else:
        return ["The dividends decreased in the last year.", 0]


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
