from urllib.request import urlopen
import json

key = "to be imported"
stock = "CVS"
what_to_extract = "balance-sheet"
what_to_extract = "cash-flow"
#what_to_extract = "income"

url = "https://financialmodelingprep.com/api/v3/" + what_to_extract + "-statement/" + stock + \
      "?limit=800&apikey=" + key

response = urlopen(url)
results = json.loads(response.read().decode("utf-8"))
print(results)

for line in results:
    print(line)
