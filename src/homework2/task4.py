"""Task4"""
import string


def main():
    """Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.

    Учитывать только английские буквы.
    """
    str_ = input("Введите любую строку: ")
    str_ = str_.replace(' ', '')
    str_ = list(str_)
    sum_l = 0
    sum_u = 0
    for letter in str_:
        if string.ascii_letters.find(letter) != -1:
            if letter.islower():
                sum_l += 1
            if letter.isupper():
                sum_u += 1
    print("Общее количество строчных(маленьких)букв равняется", sum_l)
    print("Общее количество прописных(больших)букв равняется", sum_u)


if __name__ == "__main__":
    main()