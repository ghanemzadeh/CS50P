import inflect
p = inflect.engine()

name = input ("Name: ")

while True:
    try:
        grocery = input().upper()
        if grocery in groceries:
            groceries[grocery]+=1
        else:
            groceries[grocery]=1
    except EOFError:
        print("\n")

print("Adieu, adieu, to", list)