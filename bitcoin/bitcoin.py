import sys
import requests

if len(sys.argv) == 2:
    print("Missing command-line argument")
    sys.exit
elif len(sys.argv) == 3:
    try:
        coins = float (sys.argv[2])
    except:
        print("Command-line argument is not a number")
        sys.exit

#try:
    ...
#except requests.RequestException:


