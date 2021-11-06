"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные
друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


def main():

    lst = [1, 1, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6]
    lst2 = []
    for element in lst:
        if element not in lst2:
            count_el = lst.count(element)
            lst2.append(element)
            if count_el > 1:
                count_pairs = int(count_el * (count_el - 1) / 2)
                print('Количество пар числа', element, '-', count_pairs, '.')


if __name__ == "__main__":
    main()
