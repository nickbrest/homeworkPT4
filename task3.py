# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.


from random import randint
from collections import Counter


def list_rand(count):
    if count < 0:
       print('Вводите число больш нуля!')
       return []
       
    list_rand_numb = []
    for i in range(0, count):
        list_rand_numb.append(randint(0, 10))
    return list_rand_numb


def uniq_numb(list_work):
    result = []
    list_uni_numb = Counter(list_work)
    print(list_uni_numb)
    for i in list_uni_numb:
        if list_uni_numb[i] == 1:
            result.append(i)

    return result


my_list = list_rand(int(input('Введите количество чисел в списке: ')))
print(my_list)
print(uniq_numb(my_list))
