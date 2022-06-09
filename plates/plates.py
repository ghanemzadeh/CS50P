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
                print("was it here")
                status = False
                break
            elif s[i:].isdigit() and int(c) != 0:
                status = True
                break
            else:
                print("was it here, for else")
                status = False
    else:
        print("was it here, last else")
        status = False

    return status




main()