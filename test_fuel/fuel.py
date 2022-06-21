def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()

while True:
    try:
        fraction = input ("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        percent = int(round(x/y*100))
        if percent <= 1:
           print("E")
           break
        elif 100 >= percent >= 90:
            print("F")
            break
        elif percent > 100:
            pass
        else:
            print (str(percent)+"%")
            break
    except ValueError:
        print("x/y, x or y are not intger")
        pass
    except ZeroDivisionError:
        pass

