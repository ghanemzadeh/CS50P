def main():
    while True:
        try:
            fraction = input ("Fraction: ")
            percent = convert(fraction)
            print (gauge (percent))
    except ValueError:
        print("x/y, x or y are not intger")
        pass
    except ZeroDivisionError:
        pass


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    elif x>y:
        raise ValueError

    return int(round(x/y*100))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 100 >= percentage >= 90:
        return "F"
    else:
        return str(percentage)+"%"

if __name__ == "__main__":
    main()