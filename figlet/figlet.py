import sys
from pyfiglet import Figlet
from random import choice


figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        if f not in figlet.getFonts():
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    f = choice(figlet.getFonts())
else:
    sys.exit("Invalid usage")

text = input("Input: ")
figlet.setFont(font=f)
print(figlet.renderText(text))