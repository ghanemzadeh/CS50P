filename = input ("File name: ").strip().lower()

if filename.endswith("gif","."):
    print("image/gif")
else:
    print ("application/octet-stream")