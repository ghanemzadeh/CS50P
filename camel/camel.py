string = input ("camelCase: ")

for c in string:
    if c.isupper():
        print("_", end="")
    else:
        print(c, end="")