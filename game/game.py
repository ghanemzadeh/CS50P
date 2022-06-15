from random import randrange

while True:
    level = int(input("Level: "))
    if level <= 0:
        pass

    guess = randrange(1,level+1)
    uguess = int(input("Guess: "))
    if uguess == guess:
        print("Just right!")
    elif uguess > guess:
        print("Too large!")
        pass
    else:
        print("Too small!")
        pass

    break