# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.


def FindStr(sp):
    print('Какое значение вы хотите найти?: ')
    N = input()
    if sp.count(N) == 0:
        print(f'Значение "{N}" не встречается в вашем списке.')
    else:
        print(f'Значение "{N}" присутствуют вашем списке.')

print('Введите список значений через пробел: ')
sp = input().split()
print(f'Список строк: {sp}')
FindStr(sp)