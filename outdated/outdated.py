months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
       date = input ("Date: ")
       m, d, y = date.split("/")
       m = int(m)
       d = int (d)
       #0 >= m >= 13 or 
       if 0 >= d >= 32:
           print("out")
           continue
       print (y, f"{m:02}", d, sep="-")
       break
    except ValueError:
        try:
            m, d, y = date.split(" ")
            m = months.index(m) + 1
            print (y, f"{m:02}", d, sep="-")
            break
        except ValueError:
            pass