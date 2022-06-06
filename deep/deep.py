answer= input ("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

if answer == "42":
    response ="YES"
elif answer == "forty-two":
    response ="YES"
elif answer == "forty two":
    response ="YES"
else:
    response ="No"

print(response)

