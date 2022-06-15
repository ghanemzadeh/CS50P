import inflect
p = inflect.engine()

list = ""
names = []

while True:
    try:
        name = input ("Name: ")
        names.append(name)
    except EOFError:
        print("\n")
        break

list = p.join(names)
print("Adieu, adieu, to", list)