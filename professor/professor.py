import random


def main():

    l = get_level()
    score = 0

    tries = 10
    while tries > 0:
    try:
        x = generate_integer(l)
        y = generate_integer(l)
        if three_try(x , y):
            score += 1

        tries -= 1
    except EOFError:
        print("\n")
        break

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
    if level not in [1,2,3]:
        raise ValueError

    if level == 1:
        rand_num = random.randrange(0,9)
    elif level == 2:
        rand_num = random.randrange(10,99)
    else:
        rand_num = random.randrange(100,999)

    return(rand_num)

def three_try(x , y):
    i = 3
    while i > 0:
        try:
            result = int(input(f"{x} + {y} = "))
            if result == x+y:
                return True
            else:
                i -=1
                print("EEE")
        except:
            i -=1
            print("EEE")
    print(f"{x} + {y} = ", x+y)
    return False


if __name__ == "__main__":
    main()