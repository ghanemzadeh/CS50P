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
            print (c)
            if c in ["", ",", ".","\"","'","?",";",":","!","-"]:
                status = False
                break
            elif c.isdigit() and int(c) != 0:
                    print ("digit=", c)
                    break
            else:
                status = False


    else:
        status = False

    return status




main()