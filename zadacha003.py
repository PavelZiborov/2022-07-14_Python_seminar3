# Сделать функцию, на вход принимающую список,
# а возвращая словарь с 5 элементами
# где указаны максимальное число, минимальное, ср. арифметическое)

from statistics import mean


def ListOfNumbers(text):
    print(text)
    stringFromConsole = input()
    list = []
    for i in stringFromConsole.split():
        try:
            list.append(int(i))
        except:
            print(f'Значение "{i}" не является числом и будет пропущено')
    return list


def Dictionary(list):
    D = {
        'maximum': max(list),
        'minimum': min(list),
        'arithmeticMean': mean(list)
    }
    return D


lst = ListOfNumbers('Введите числа разделяя их пробелами: ')
print(lst)
biblioteka = Dictionary(lst)
print(biblioteka.items())

with open('HW1.txt', 'a') as file:
    file.write(f'Для {lst} - ')
    for a, b in biblioteka.items():
        file.write(f'{a} = {b}.  ')
    file.write('\n')
