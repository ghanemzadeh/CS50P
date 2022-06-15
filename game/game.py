from random import randrange

while True:
    level = int(input("Level: "))
    if level <= 0:
        pass

    guess= randrange(1,level+1)
    print("Guess: ",guess)
    break