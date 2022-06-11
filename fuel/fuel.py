

i=1
while True:
    try:
        fraction = input ("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        percent = int(x/y*100)
        if percent <= 1:
           print("E")
        elif percent >= 90:
            print("F")
        else:
            print (str(percent)+"%")
    except ValueError:
        print("x/y, x or y are not intger")
        pass
    except ZeroDivisionError:
        pass
    i+=1
