import sys
import requests

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit
elif len(sys.argv) == 2:
    try:
        coins = float (sys.argv[2])
    except:
        print("Command-line argument is not a number")
        sys.exit
    print("coins = ", coins)

#try:
    ...
#except requests.RequestException:


