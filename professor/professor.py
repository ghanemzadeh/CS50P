import random


def main():
    l = get_level()
    #print("level is:", l)
    #print("int is:", generate_integer(l))

    score = 0
    for _ in range(10):
        x = generate_integer(l)
        y = generate_integer(l)
        xy = str(x) + " + " + str(y) + " = "
        result = int(input(xy))
        if result == x+y:
            score += 1
        else:
            i = 2
            while i > 0:
                print ("EEE")
                result = int(input(xy))
                if result == x+y:
                    score += 1
                    break
                else:
                    i -=1
            print (xy, x+y)

    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except ValueError:
            continue

    return level


def generate_integer(level):
    if level <= 0 or level > 3:
        raise ValueError

    if level == 1:
        start = 0
        end = 9
    elif level == 2:
        start = 10
        end = 99
    else:
        start = 100
        end = 999

    return(random.randrange(start,end))


if __name__ == "__main__":
    main()