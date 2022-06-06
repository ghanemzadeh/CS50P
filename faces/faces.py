def main():
    emoticon = input("What's your emoticon? ")
    convert(emoticon)


def convert(to):
    if to == ":)":
        emoji = "🙂"
    elif to == ":(":
        emoji = "🙁"
    else:
        emoji = to

    print(to, "= ", emoji)


main()