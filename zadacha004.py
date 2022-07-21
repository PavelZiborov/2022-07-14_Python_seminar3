# Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
# сохраните список в формате JSON.

import json


def InputNumbers():
    print('Введите число: ')
    N = int(input())
    return N

def CreateList (N):
    list = []
    for i in range(-N, N+1):
        list.append(i)
    return list

N = InputNumbers()
list = CreateList(N)
print(list)

with open('listOfNumbers.json', 'w', encoding='utf-8') as data:  # загрузка списка в файл listOfNumbers.json
    data.write(json.dumps(list))
    data.write('\n')
print('Лист успешно сохранен в файл')

with open('listOfNumbers.json', 'r', encoding='utf-8') as data:  # открываем файл на чтение
    BD = json.load(data)                                         # загружаем из файла данные в словарь data
print(f'Загружена информация из файла: {BD}')