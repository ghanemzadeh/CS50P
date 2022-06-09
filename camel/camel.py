string = input ("camelCase: ")


for c in string:
    if c.isupper():
        print("_" + c.lower(), end = "")
    else:
        print(c, end = "")

print()
