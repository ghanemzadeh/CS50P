def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6 :
        return False
    elif s[0:2].isalpha():
        print (s[0:2])
        return True
    else:
        return False


main()