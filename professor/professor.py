import random


def main():
    print("level is:", get_level())


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


if __name__ == "__main__":
    main()