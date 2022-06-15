from random import randrange

while True:
    level = int(input("Level: "))
    if level <= 0:
        pass
    break

guess = randrange(1,level+1)

while True:
    try:
        uguess = int(input("Guess: "))
        if uguess <= 0:
            print("negative")
            continue
    except ValueError:
        pass

    if uguess == guess:
        print("Just right!")
        break
    elif uguess > guess:
        print("Too large!")
        pass
    else:
        print("Too small!")
        pass


