import sys
import requests
coins = 0
if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit
elif len(sys.argv) == 2:
    try:
        coins = float (sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit
    print("coins = ", coins)

try:
    response = requests.get(
    "https://api.coindesk.com/v1/bpi/currentprice.json"
)
    result = response.json()
    rate = result["bpi"]["USD"]["rate"]
    rate = rate.replace (",","")
    print (rate)
    rate = float(rate)
    print (rate)
except requests.RequestException:
     sys.exit

