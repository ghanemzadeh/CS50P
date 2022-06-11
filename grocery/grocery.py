groceries = {
}

total = 0
while True:

    try:
        grocery = input("Item: ").upper()
        if grocery in groceries:
            groceries[grocery]+=1
        else:
            groceries.update({grocery:1})
    except EOFError:
        print("\n")
        break
    except KeyError:
        pass
dict(sorted(groceries.items(), key=lambda item: item[0]))

for grocery in groceries:
    print(groceries[grocery], grocery)