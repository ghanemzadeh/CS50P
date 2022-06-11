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
       if 1 > m > 12 and 1 > d >31:
           continue
       print (y, "-", f"{m:02}","-", d)
       break
    except ValueError:
        m, d, y = date.split(",")
        print("valeue")
        mm = months.index(m)
        print("index", mm)
        pass