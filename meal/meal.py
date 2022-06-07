def main():
    time = input("What time is it? ")

    coverted = convert(time)
    
    if 7.0 <= coverted <= 8.0:
        print("breakfast time")


def convert(time):
    h , m = time.split(":")
    print (h,m)
    return h+ (m*10/6)


if __name__ == "__main__":
    main()