def main():
    """Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.

    Если стороны определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных.
    """
    a1 = float(input("Введите первую сторону треугольника (см): "))
    b1 = float(input("Введите вторую сторону треугольника (см): "))
    c1 = float(input("Введите третью сторону треугольника (см): "))
    if a1 < (b1 + c1) and b1 < (a1 + c1) and c1 < (a1 + b1):
        p = (a1 + b1 + c1) / 2   # полупериметр
        s = (p * (p - a1) * (p - b1) * (p - c1)) ** 0.5   # площадь треугольника по формуле Герона
        print("Площадь треугольника равняется (см2)", s)
    else:
        print("Неверные данные")


if __name__ == "__main__":
    main()
