groceries = {
}

total = 0
while True:

    try:
        item = input("Item: ").title()
        if grocery in groceries:
            price = float (items[item])
            total +=round(price, 2)
            print("total: ", f"${total:.2f}")
        else:
            
    except EOFError:
        print("\n")
        break
    except KeyError:
        pass