import sys
from pyfiglet import Figlet
from random import choice

text = input("Input: ")
figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
    else:
        print("Invalid usage")
        sys.exit
elif len(sys.argv) == 1:
    f = choice(figlet.getFonts())

figlet.setFont(font=f)
print(figlet.renderText(text))