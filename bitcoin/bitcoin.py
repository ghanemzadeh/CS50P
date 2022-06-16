import sys
import requests

print ("we are in")
if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit
elif len(sys.argv) == 2:
    try:
        coins = float (sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit


try:
    response = requests.get(
    "https://api.coindesk.com/v1/bpi/currentprice.json"
)
    result = response.json()
    rate = result["bpi"]["USD"]["rate"]
    rate = rate.replace (",","")
    rate = float(rate)
    exchange = coins * rate
    print (f"${exchange:,}")
except requests.RequestException:
     sys.exit

