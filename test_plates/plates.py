def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    status = True
    if len(s) < 2 or len(s) > 6 :
        status = False
    elif s[0:2].isalpha():
        for c in s[2:len(s)]:
            i = s.index(c)
            if c in [" ", ",", ".","\"","'","?",";",":","!","-"]:
                return False
                break
            elif s[i:].isalpha():
                return True
            if s[i:].isdigit() and int(c) != 0:
                return True
            elif c.isalpha():
                break
            else:
                return False
    else:
        status = False

    return status


if __name__ == "__main__":
    main()