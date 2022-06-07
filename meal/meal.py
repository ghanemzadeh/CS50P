def main():
    time = input("What time is it? ")

    convert(time)
    coverted = 7.1
    if 7.0 <= coverted <= 8.0:
        print("breakfast time")


def convert(time):
    h , m = time.split(":")
    print (h,m)
    return h+


if __name__ == "__main__":
    main()