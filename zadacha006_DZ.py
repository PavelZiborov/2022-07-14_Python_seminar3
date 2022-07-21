# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


# print('Введите список значений через пробел: ')
# sp = input().split()

sp1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
sp2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
sp3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
sp4 = ["123", "234", 123, "567"]
sp5 = []


def FindIndex(sp):
    fnd = input('Что ищем: ')
    sp_index = []
    for i in range(0, len(sp)):
        if sp[i] == fnd:
            sp_index.append(i)
    if len(sp_index) < 2:
        return -1
    else:
        return sp_index[1]  # индекс второго вхождения


# print(f'Индекс второго вхождения = {FindIndex(sp)}')
print(f'Индекс второго вхождения = {FindIndex(sp1)}')
print(f'Индекс второго вхождения = {FindIndex(sp2)}')
print(f'Индекс второго вхождения = {FindIndex(sp3)}')
print(f'Индекс второго вхождения = {FindIndex(sp4)}')
print(f'Индекс второго вхождения = {FindIndex(sp5)}')