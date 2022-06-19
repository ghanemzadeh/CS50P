def main():
    string = input ("Input: ")
    print(shorten (string))


def shorten(word):
    new_str = ""
    for c in word:
        if c in ["A", "a", "e", "E", "i", "I", "o", "O", "u", "U"]:
            continue
        new_str += c

    return new_str



if __name__ == "__main__":
    main()

