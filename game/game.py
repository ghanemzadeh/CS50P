from random import randrange

Flag = True
While Flag:
    level = int(input("Level: "))
    if level <= 0:
        pass

    guess= random.randrange(level)
    print("Guess: ",guess)
    Flag = False