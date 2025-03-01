"""
Используйте генератор списков чтобы получить следующий: ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента не было.
"""


def main():
    list1 = [i + q for i in "ab" for q in "bcd"]
    list2 = list1[::2]
    print(list2)
    list3 = [str(i) + "a" for i in range(1, 5)]
    print(list3.pop(1))
    list4 = list3.copy()
    list4.append("2a")


if __name__ == "__main__":
    main()
