fraction = input ("Fraction: ")
x, y = fraction.split("/")
try:
    x = int(x)
    y = int(y)
    print (int(x/y*100),"%")
except ValueError:
    print("x/y, x or y are not intger")
except ZeroDivisionError:
    print("x/y, y should not be zero")
