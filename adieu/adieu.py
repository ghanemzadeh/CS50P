import inflect
p = inflect.engine()

list =""

while True:
    try:
        name = input ("Name: ")
        list = p.join((list, name))
    except EOFError:
        print("\n")

print("Adieu, adieu, to", list)