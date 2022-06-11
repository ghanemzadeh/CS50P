fraction = input ("Fraction: ")
x, y = fraction.split("/")
try:
    x = int(x)
    y = int(y)
    print (x,y)
except ValueError:
    print("x/y, x or y are not intger")
except ZeroDivisionError:
    print("x/y, y should not be zero")
