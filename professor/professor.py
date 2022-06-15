import random


def main():
    l = get_level()
    print("level is:", l)
    print("int is:", generate_integer(l))

    score = 0
    for in in range(10):
        

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 4 > level > 0:
                break
        except ValueError:
            continue

    return level


def generate_integer(level):
    if level <= 0 or level > 3:
        raise ValueError

    if level == 1:
        start = 1
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