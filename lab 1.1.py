def read_file():
    while True:
        path = input("Введите путь к файлу: ").strip()
        try:
            with open(path, encoding='utf-8') as f:
                data = f.readlines()
                return data
        except FileNotFoundError:
            print("Файл не найден!", '\n')
        except ValueError:
            print("Неправильный формат файла!", '\n')

def remove_double(textkey, abc):
    for symbol in textkey:
        if textkey.count(symbol) > 1:
           textkey.remove(symbol)
        if symbol in abc:

           abc.remove(symbol)

    print(textkey)
    return abc, textkey


def change_abc(keyword, abc, index):
    new_abc = list()
    i = 0
    k = 0

    for symbol in keyword:
        new_abc.append(symbol)

    #for symbol in abc:
    #    new_abc.append(symbol)

    for i in range(len(abc) - index):
        new_abc.append(abc[i])
        i += 1

    for i in range(len(abc) - index, len(abc)):
        new_abc.insert(k, abc[i])
        i += 1
        k += 1

    return new_abc


def encrypt(text, mode, abc, shifted_abc, final =""):
    if mode == 'ш':
        for symbol in text:
            if symbol == ".": final += "."
            elif symbol == ",": final += ","
            elif symbol == "?": final += "?"
            elif symbol == "!": final += "!"
            elif symbol == "/": final += "/"
            elif symbol == ":": final += ":"
            elif symbol == ";": final += ";"
            elif symbol == "-":  final += "-"
            elif symbol == "–": final += "–"
            elif symbol == "\"": final += "\""
            elif symbol == "\n": final += ""
            elif symbol == " ": final += " "
            else:
                index = abc.index(symbol.upper())
                #final += abc[(abc.index(symbol.upper()) + key)%32]
                final += shifted_abc[index]

    if mode == 'д':
        for symbol in text:
            if symbol == ".": final += "."
            elif symbol == ",": final += ","
            elif symbol == "?": final += "?"
            elif symbol == "!": final += "!"
            elif symbol == "/": final += "/"
            elif symbol == ":": final += ":"
            elif symbol == ";": final += ";"
            elif symbol == "-": final += "-"
            elif symbol == "–":  final += "–"
            elif symbol == "\"": final += "\""
            elif symbol == "\n": final += ""
            elif symbol == " ": final += " "
            else:
                #final += abc[(abc.index(symbol.upper()) - key)%32]
                index = shifted_abc.index(symbol.upper())
                final += abc[index]

    return final


if __name__ == '__main__':

    alphabet = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

    # Алфавит для сдвига
    abc = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

    key = ""
    mode = ""
    text_key = ""
    print_text = list()

    # Считываем текст с файла
    text = read_file()

    print(f'Исходный текст: ')
    for line in text:
        print(line, end='')

    print()
    while True:
        mode = input("Введите 'ш' для шифрования или 'д' для дешифровки: ")
        if mode == "ш" or mode == "д":
            break
        print("Выбран неправильный режим!", '\n')

    key = int(input("Введите ключ: "))

    text_key = list(input("Введите ключевое слово: ").upper())

    new_abc, new_word = remove_double(text_key, abc)

    shifted_abc = change_abc(new_word, new_abc, key)
    print(shifted_abc)

    for line in text:
        result = encrypt(line, mode, alphabet, shifted_abc)
        print(result.lower())
