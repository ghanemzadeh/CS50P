import sys
from pyfiglet import Figlet

text = input("Input: ")
figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
elif len(sys.argv) == 1:
    print ("fonts: ",random.choice(figlet.getFonts()))
    f = "slant"

figlet.setFont(font=f)
print(figlet.renderText(text))