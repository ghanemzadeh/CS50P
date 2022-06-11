fraction = input ("Fraction: ")
x, y = fraction.split("/")
x = int(x)
y = int(y)

while True:
    try:
        percent = int(x/y*100)
        if percent <= 1:
           print("E")
        elif percent >= 90:
            print("F")
        else:
            print (str(percent)+"%")
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
