filename = input ("File name: ").strip().lower()

if filename.endswith("gif"):
    print("image/gif")
elif filename.endswith("jpg") or filename.endswith("jpeg"):
    print("image/jpg")
elif filename.endswith("png"):
    print("image/png")
else:
    print ("application/octet-stream")