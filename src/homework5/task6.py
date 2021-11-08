"""
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""


def main():

    str_ = input('Введите строку текста: ')
    words = []
    lst = str_.splitlines()
    for n in lst:
        parts = n.split()
        for part in parts:
            words.append(part)
    set_ = set(words)
    print(len(set_))


if __name__ == "__main__":
    main()