def main():
    time = input("What time is it? ")

    coverted = convert(time)

    if 7.0 <= coverted <= 8.0:
        print("breakfast time")


def convert(time):
    h , m = time.split(":")
    h = float (h)
    m = float (m)
    print ("h+ (m/60) =", h+ (m/6))

    return h+ (m/6)


if __name__ == "__main__":
    main()