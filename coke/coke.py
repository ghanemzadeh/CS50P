due = 50
while due> 0:
    print("Amount Due: ", due)
    coin = int(input("insert coin: "))
    if coin > due:
        change = coin - due
    due-= coin

print ("Change owed: ", change)