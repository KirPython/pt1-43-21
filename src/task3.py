"""
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
"""
def main():
    s = input('Введите предложение: ')
    s = s.replace(' ', '')
    s = list(s)
    new_s = ''
    for n in s:
        if new_s.find(n) == -1:
            new_s = new_s + n
    print(new_s)
    if __name__ == "__main__":
    main()
