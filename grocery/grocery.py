groceries = {}

while True:
    try:
        grocery = input().upper()
        if grocery in groceries:
            groceries[grocery]+=1
        else:
            groceries[grocery]=1
    except EOFError:
        print("\n")
        for grocery in sorted (groceries.keys()):
            print(groceries[grocery], grocery)
        break
    except KeyError:
        pass