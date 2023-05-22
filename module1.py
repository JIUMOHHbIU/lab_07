"""
Жиляев Антон ИУ7-14Б
Программа удаляет все чётные элементы целочисленного списка
"""

# Ввод целочисленного списка
a = list(map(int, input('Введите все элементы целочисленного списка через пробел:\n').split(' ')))

# Оставляем все нечётные элементы
k = 0
for i in range(len(a)):
    if a[i] % 2:
        a[k] = a[i]
        k += 1
a = a[:k]

# Вывод полученного списка
print('\nИзменённый список:')
print(*a)
