"""
Жиляев Антон ИУ7-14Б
Программа ищет в списке строк элемент с наибольшим количеством подряд идущих цифр
"""

# Все цифры
NUMBERS_DECIMAL = set(str(i) for i in range(10))

# Ввод списка строк
while True:
    n = int(input('Введите размер списка строк: '))
    if n > -1:
        break
    print('Размер списка должен быть неотрицательным')

a = [''] * n
for i in range(n):
    a[i] = input(f'Введите {i+1}-ю строку:\n')

# Нахождение строки с наибольшим количеством подряд идущих цифр
max_seqnumbers_element = (-1, -1)
for i in range(n):
    current_length = max_current_length = 0
    for value in a[i]:
        if value in NUMBERS_DECIMAL:
            current_length += 1
            max_current_length = max(max_current_length, current_length)
            if max_current_length > max_seqnumbers_element[0]:
                max_seqnumbers_element = (max_current_length, i)
        else:
            current_length = 0

if max_seqnumbers_element[1] == -1:
    print('\nПустой список строк, невозможно найти строку с наибольшим количеством подряд идущих чисел')
# Вывод искомой строки
print('\nСтрока с наибольшим количеством подряд идущих чисел:')
print(a[max_seqnumbers_element[1]])
