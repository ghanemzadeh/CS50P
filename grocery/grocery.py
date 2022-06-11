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
        print()
        break
    except KeyError:
        pass

#print (groceries)

for grocery in sorted (groceries.keys()):
    print(groceries[grocery], grocery)