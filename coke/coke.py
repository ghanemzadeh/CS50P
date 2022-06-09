due = 50
while due> 0:
    print("Amount Due ", due)
    coin = int(input("insert coin: "))
    due-= coin
print ("Change owed", coin-due)