# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести
# получившуюся статистику.

# Программа должна считывать одну строку со стандартного ввода и выводить для каждого
# уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

# Sample Input 1:
# a aa abC aa ac abc bcd a

# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2

# Sample Input 2:
# a A a

# Sample Output 2:
# a 3


from itertools import count

str1 = 'a aa abC aa ac abc bcd a'
str2 = 'a A a'

def FindUniqueValues(text):
    list = text.lower().split() # ['a', 'aa', 'abc', 'aa', 'ac', 'abc', 'bcd', 'a'] - список строк без учета регистра
    unique_list = set(list)     # {'a', 'aa', 'bcd', 'ac', 'abc'}
    for i in unique_list:
        print(i, list.count(i))

print(f'Для строки: "{str1}": ')
FindUniqueValues(str1)
print(f'Для строки: "{str2}": ')
FindUniqueValues(str2)
