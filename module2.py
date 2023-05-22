"""
Жиляев Антон ИУ7-14Б
Программа вставляет после каждого положительного элемента его удвоенное значение в целочисленном списке
"""

# Ввод целочисленного списка
a = list(map(int, input('Введите все элементы целочисленного списка через пробел:\n').split(' ')))

# Подсчёт количества положительных элементов
counter_positive = 0
for el in a:
    counter_positive += el > 0

# Расширение списка для вставки
a += [None] * counter_positive

# Вставка удвоенных значений
sample_position = len(a) - counter_positive - 1
is_double_element = 0
for insert_position in range(len(a) - 1, -1, -1):
    # Проверяем, положительный ли это элемент и впервые ли мы смотрим на этот положительный элемент
    is_double_element = (a[sample_position] > 0) and not is_double_element

    a[insert_position] = a[sample_position] * (1 + is_double_element)
    # Если удвоенное значение элемента вставлено или это отрицательный элемент,
    # тогда переходим к следующему элементу к переносу в суффикс списка
    sample_position -= not is_double_element

# Вывод полученного списка
print('\nИзменённый список:')
print(*a)
