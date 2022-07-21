sp = [5, 11, 2, 3, 4, 8, 157, 555]


def max_average(sp):
    max = sp[0]
    sr = 0
    for i in sp:
        if i > max:
            max = i
        sr += i
    sr = sr/len(sp)
    rez = {}
    rez['максимальный элемент'] = max
    rez['среднее арифметическое'] = sr
    k = (max, sr, rez)
    return k


res = max_average(sp)
# print(res[2])
for x, y in res[2].items():
    print(x, y)


import json

with open('data.json', 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD = json.load(fh)                    # загружаем из файла данные в словарь data
print('БД успешно загружена')
print(type(BD))