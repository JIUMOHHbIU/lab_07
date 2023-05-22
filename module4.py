"""
Жиляев Антон ИУ7-14Б
Программа заменяет все строчные гласные английские буквы на заглавные
"""

# Словарь перевода нижнего регистра английского алфавита в верхний
ASCII_LOWERVOWEL_TO_UPPERVOWEL = dict(zip('aeiou', 'AEIOU'))

# Ввод списка строк
while True:
    n = int(input('Введите размер списка строк: '))
    if n > -1:
        break
    print('Размер списка должен быть неотрицательным')

a = [''] * n
for i in range(n):
    a[i] = input(f'Введите {i+1}-ю строку:\n')

# Замена соответствующих элементов
for i in range(n):
    a[i] = ''.join([ASCII_LOWERVOWEL_TO_UPPERVOWEL.get(value, value) for value in a[i]])

# Вывод измененного списка строк
print('\nИзменённый список строк:')
print(*a, sep='\n')
