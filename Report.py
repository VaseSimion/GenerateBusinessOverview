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


def write_data(file, data, profile):


    file.write("""<h1>{}</h1>

    <p>Price is {}$ per share</p>
    <br>
    <p>The P/E ratio according to last yearly earnings is {}</p>
    <p> It operates in the {} sector, part of the {} industry.</p
    """.format(profile["companyName"], profile["price"], round(profile["price"]/data["EPS"][-1], 1), profile["sector"], profile["industry"]) +
               "<p>" + Nt.free_cash_flow_analysis(data)[0]+"</p>" +
               "<p>" + Nt.revenue_analysis(data)[0] + "</p>" +
               "<p>" + Nt.net_income_analysis(data)[0] + "</p>" +
               "<p>" + Nt.roe_analysis(data)[0] + "</p>" +
               "<p>" + Nt.profit_margin_analysis(data)[0] + "</p>" +
               "<p>" + Nt.dividends_analysis(data)[0] + "</p>" +
               """
    <p> You can find more information on stock at <a href=https://finance.yahoo.com/quote/{}>{}</a> </p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}-price.png" width="800" height="426"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Revenue.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Free cash flow.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Current EquityShareholder Equity.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}DebtShareholder Equity.png" width="800" height="214"></p>
    <p><img src="C:/Users/sular/PycharmProjects/Generate Business Overview/Support Files/{}Dividends paid.png" width="800" height="214"></p>
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
                   data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"], data["Symbol"]))


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
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <p>Disclaimer: This is just a financial experiment, I am in no position to give financial advice. I have no education in finance and you should do your investing and trading based on your own due dilligence and research.</p>
    </body>
    </html>""")


def write_the_report(data, profile):
    report_name = "Support Files/Temporary.html"
    template_file = open(report_name, "w+")
    write_start(template_file)
    write_data(template_file, data, profile)
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

"""
    <table style="width:800px">
      <tr>
        <th></th>
        <th>{}</th>
        <th>{}</th>
        <th>{}</th>
        <th>{}</th>
      </tr>
      <tr>
        <td>Income before tax</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>Gross profit</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>Total revenue</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
      </tr>
    </table>
"""
