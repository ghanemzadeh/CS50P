import inflect
p = inflect.engine()

list = ""


while True:
    try:
        name = input ("Name: ")
        list = p.join((list, name), final_sep="")
    except EOFError:
        print("\n")
        break

print("Adieu, adieu, to", list)