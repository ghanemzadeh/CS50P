groceries = {
}

total = 0
while True:

    try:
        item = input("Item: ").title()
        if item in items:
            price = float (items[item])
            total +=round(price, 2)
            print("total: ", f"${total:.2f}")
    except EOFError:
        print("\n")
        break
    except KeyError:
        pass