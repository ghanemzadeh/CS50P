import inflect
p = inflect.engine()

list = ""


while True:
    try:
        name = input ("Name: ")
        list = list + p.join((name))
        print("list is=", list)
    except EOFError:
        print("\n")
        break

print("Adieu, adieu, to", list)