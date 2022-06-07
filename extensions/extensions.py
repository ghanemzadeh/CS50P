filename = input ("File name: ").strip().lower()

if filename.endswith("gif"):
    print("image/gif")
elif filename.endswith("jpg") or filename.endswith("jpeg"):
    print("image/jpg")
else:
    print ("application/octet-stream")