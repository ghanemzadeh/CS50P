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
       if d > 31 or m >12:
           continue
       print (y, f"{m:02}", f"{d:02}", sep="-", end="")
       break
    except ValueError:
        try:
            m, d, y = date.split(" ")
            d = int (d)
            m = months.index(m) + 1
            if d > 31 or m >12:
                continue
            print (y, f"{m:02}", f"{d:02}", sep="-", end="")
            break
        except ValueError:
            pass