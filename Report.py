import yfinance as yf
import GraphFunctions as Gf
import time
import pdfkit
import re
import os
from datetime import date
import pandas as pd
import numpy as np
import NumbersToText as Nt


def write_start(file):
    file.write("""<!DOCTYPE html>
        <html>
        <head>
        <title>Analysis</title>
        <style>
        table, th, td {
          border: 1px solid black;
        }
        </style>
        </head>
        <body>
        """)


def write_data_fmp(file, data, profile):
    file.write("""<h1>{}</h1>

    <p>Price is {}$ per share</p>
    <br>
    <p>The P/E ratio according to last yearly earnings is {}</p>
    <p>The company has a market cap of {} billion</p>
    <p> It operates in the {} sector, part of the {} industry.</p
    """.format(profile["companyName"], profile["price"], round(profile["price"] / data["EPS"][-1], 1),
               round(profile['mktCap'] * 1e-9, 2), profile["sector"], profile["industry"]) +
               "<p>" + Nt.free_cash_flow_analysis(data)[0] + "</p>" +
               "<p>" + Nt.revenue_analysis(data)[0] + "</p>" +
               "<p>" + Nt.net_income_analysis(data)[0] + "</p>" +
               "<p>" + Nt.roe_analysis(data)[0] + "</p>" +
               "<p>" + Nt.profit_margin_analysis(data)[0] + "</p>" +
               "<p>" + Nt.simple_free_cash_flow_prediction(data) + "</p>" +
               "<p>" + Nt.extrapolated_free_cash_flow_prediction(data) + "</p>" +
               """
    <p> You can find more information on stock at <a href=https://finance.yahoo.com/quote/{}>{}</a> </p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}-price.png" width="800" height="426"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Revenue.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Free cash flow.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Current EquityShareholder Equity.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}DebtShareholder Equity.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Dividends per share.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Earnings per share.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Net income.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Profit margin.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Return on equity.png" width="800" height="214"></p>        
    <br>
    <br>,
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>""".format(data["Symbol"], data["Symbol"],
                   data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"],
                   data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"]))


def write_data_quickfs(file, data, profile):
    file.write("""<h1>{}</h1>

    <p>Price is {}$ per share</p>
    <br>
    <p>The P/E ratio according to last yearly earnings is {}</p>
    <p>The company has a market cap of {} billion</p>
    <p> It operates in the {} sector, part of the {} industry.</p
    """.format(profile["companyName"], profile["price"], round(profile["price"] / data["EPS"][-1], 1),
               round(profile['mktCap'] * 1e-9, 2), profile["sector"], profile["industry"]) +
               "<p>" + Nt.free_cash_flow_analysis(data)[0] + "</p>" +
               "<p>" + Nt.revenue_analysis(data)[0] + "</p>" +
               "<p>" + Nt.net_income_analysis(data)[0] + "</p>" +
               "<p>" + Nt.roe_analysis(data)[0] + "</p>" +
               "<p>" + Nt.profit_margin_analysis(data)[0] + "</p>" +
               "<p>" + Nt.simple_free_cash_flow_prediction(data) + "</p>" +
               "<p>" + Nt.extrapolated_free_cash_flow_prediction(data) + "</p>" +
               "<p>" + Nt.calculated_sticker_price_according_to_rule_1_book(data) + "</p>" +
               """<table style="width:800px">
      <tr>
        <th></th>
        <th>ROIC median</th>
        <th>Equity growth</th>
        <th>EPS growth</th>
        <th>FCF growth</th>
      </tr>
      <tr>
        <td>10 year average</td>
        <td>{}%</td>
        <td>{}%</td>
        <td>{}%</td>
        <td>{}%</td>
      </tr>
      <tr>
        <td>5 year average</td>
        <td>{}%</td>
        <td>{}%</td>
        <td>{}%</td>
        <td>{}%</td>
      </tr>
      <tr>
        <td>Last year</td>
        <td>{}%</td>
        <td>{}%</td>
        <td>{}%</td>
        <td>{}%</td>
      </tr>
    </table>
    """.format(data["10yAverage"][0], data["10yAverage"][1], data["10yAverage"][2], data["10yAverage"][3],
               data["5yAverage"][0], data["5yAverage"][1], data["5yAverage"][2], data["5yAverage"][3],
               data["lastYearAverage"][0], data["lastYearAverage"][1], data["lastYearAverage"][2],
               data["lastYearAverage"][3]) +
               """
    <p> You can find more information on stock at <a href=https://finance.yahoo.com/quote/{}>{}</a> </p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}-price.png" width="800" height="426"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Revenue.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Free cash flow.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Current EquityShareholder Equity.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}DebtShareholder Equity.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Dividends per share.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Earnings per share.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Net income.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Profit margin.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Return on equity.png" width="800" height="214"></p>        
    <br>""".format(data["Symbol"], data["Symbol"],
                   data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"],
                   data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"]))


def write_end(file):
    file.write(
        """    
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <p>Disclaimer:The information on this page, and its related publications, is not intended to be, nor does it constitute, investment advice or recommendations. In no event shall the author be liable to any member, guest, or third party for any damages of any kind arising out of the use of any content or other material published or available on this page, or relating to the use of, or inability to use, this page or any content. The information on this page is not guaranteed for completeness, accuracy, or in any other way.</p>
    </body>
    </html>""")


def write_the_report(data, profile):
    report_name = "Support Files/Temporary.html"
    template_file = open(report_name, "w+")
    write_start(template_file)
    if data["Source"] == "FinancialModelingPrep":
        write_data_fmp(template_file, data, profile)
    elif data["Source"] == "QuickFS":
        write_data_quickfs(template_file, data, profile)
    write_end(template_file)
    template_file.close()

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    options = {'enable-local-file-access': None}
    pdfkit.from_file('Support Files\\Temporary.html', 'Reports/Report ' + str(data["Symbol"]) + '.pdf',
                     configuration=config, options=options)

    supportdir = "Support Files"

    for subdir, dirs, files in os.walk(supportdir):
        for file in files:
            print(os.path.join(subdir, file))
            os.remove(os.path.join(subdir, file))
