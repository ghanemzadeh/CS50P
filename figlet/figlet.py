import sys
from pyfiglet import Figlet
from random import choice

text = input("Input: ")
figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        if f not in figlet.getFonts():
            sys.exit("Invalid usage")
    else:
        print("point 2")
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    f = choice(figlet.getFonts())
    print("point 3")
else:
    print("point 4")
    sys.exit("Invalid usage")


figlet.setFont(font=f)
print(figlet.renderText(text))