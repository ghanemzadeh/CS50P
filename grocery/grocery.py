groceries = {
}

total = 0
while True:

    try:
        grocery = input("Item: ").title()
        if grocery in groceries:
            groceries[grocery]+=1
            total +=round(price, 2)
            print("total: ", f"${total:.2f}")
        else:

    except EOFError:
        print("\n")
        break
    except KeyError:
        pass