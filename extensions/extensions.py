filename = input ("File name: ").strip().lower()

if filename.endswith("gif"):
    print("image/gif")
elif filename.endswith("jpg") or filename.endswith("jpeg"):
    print("image/jpg")
elif filename.endswith("png"):
    print("image/png")
elif filename.endswith("pdf"):
    print("application/pdf")
elif filename.endswith("pdf"):
    print("application/pdf")
else:
    print ("application/octet-stream")