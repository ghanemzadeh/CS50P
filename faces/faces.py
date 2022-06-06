def main():
    emoticon = input("What's your emoticon? ")
    convert(emoticon)


def convert(to=":)"):
    if to == ":)":
        emoji = "🙂"
    print(to, "= ", emoji)


main()