def main():
    emoticon = input("What's your emoticon? ")
    convert(emoticon)


def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    print(text)


main()