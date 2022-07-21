# 3. Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# *Пример:*
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Задайте список из n чисел ряда фибоначи, возвращает список

from ast import For, While


def InputNumbers():
    print('Введите число: ')
    N = int(input())
    return N

# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# data = list(fibonacci(N))
# print(data)

def fibo(n):
    if n in [1,2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibolist(x):
    list = []
    for i in range(1, x+1):
        list.append(fibo(i))
    return list
    

N = InputNumbers()
print(N)
print(fibolist(N))





