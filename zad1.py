from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления'
           'квадратного корня из заданного числа.')
print(message)


def calculatesquareroot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Получим результат."""
    if your_number > 0:
        root = calculatesquareroot(your_number)
        print('Мы вычислили квадратный корень из введённого вами числа.'
              f'Это будет {root}')
    print(message)
    calc(25.5)