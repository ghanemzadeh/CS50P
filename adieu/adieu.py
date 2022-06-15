import inflect
p = inflect.engine()

list = ""


while True:
    try:
        name = input ("Name: ")
        list = p.join((list, name))
        print("list is=", list)
    except EOFError:
        print("\n")
        break

print("Adieu, adieu, to", list)