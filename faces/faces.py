def main():
    emoticon = input("What's your emoticon? ")
    convert(emoticon)


def convert(text):
    emoji = text.replace(":)", "🙂")
    emoji = text.replace(":(", "🙁")
    print(text, "= ", emoji)


main()