def main():
    time = input("What time is it? ")

    coverted = convert(time)

    if 7.0 <= coverted <= 8.0:
        print("breakfast time")
    elif 12.0 <= coverted <= 13.0:
        print("lunch time")
    elif 18.0 <= coverted <= 19.0:
        print("dinner time")


def convert(time):
    h , m = time.split(":")
    h = float (h)
    m = float (m)

    return round(h+ m/60, 1)


if __name__ == "__main__":
    main()