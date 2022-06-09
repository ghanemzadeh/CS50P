string = input ("Input: ")

new_str = ""
for c in string:
    if c in ["A", "a", "e", "E", "i", "I", "o", "O", "u", "U"]:
        continue
    new_str += c
print (new_str)