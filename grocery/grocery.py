groceries = {
}

total = 0
while True:

    try:
        grocery = input("Item: ").upper()
        if grocery in groceries:
            groceries.update({grocery:})
            groceries[grocery]+=1
            total +=round(price, 2)
            print("total: ", f"${total:.2f}")
        else:

    except EOFError:
        print("\n")
        break
    except KeyError:
        pass