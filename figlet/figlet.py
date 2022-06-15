import sys
from pyfiglet import Figlet

text = input("Input: ")

if len(sys.argv) == 2:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = Figlet(font=sys.argv[2])
        print f.renderText(text)
