from translate import Translator


def main():
    while True:
        from_language = input("origin language: ")
        if len(from_language.strip()) > 0:
            break
        else:
            print("language required")
            continue

    while True:
        to_language = input("translate language to: ")
        if len(to_language.strip()) > 0:
            break
        else:
            print("language required")
            continue

    while True:
        phrase = input("Phrase to translate: ")
        if len(phrase.strip()) > 0:
            break
        else:
            print("phrase required")
            continue

    translator = Translator(from_lang=from_language, to_lang=to_language)
    translation = translator.translate(phrase)

    with open('./translated.txt', mode='a', encoding="utf-8") as my_file:
        my_file.write(
            f'{from_language}: {phrase}, {to_language}: {translation}\n')


if __name__ == "__main__":
    main()
