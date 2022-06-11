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
       if m > 12:
           continue
       print (y, "-", f"{m:02}","-", d)
       break
    except ValueError:
        print("valeue")
        pass