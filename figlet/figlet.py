import sys
from pyfiglet import Figlet

text = input("Input: ")

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        figlet = Figlet(font=sys.argv[2])
        figlet.setFont(font=f)
        print(figlet.renderText(text))
elif len(sys.argv) == 1:
    figlet = Figlet()
    print(figlet.renderText(text))