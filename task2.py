# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


from math import sqrt


def simple_mult(n):
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            result.append(i)
            n //= i 
    if n != 1: 
        result.append(n)
    return(result)


number = int(input('Введите число: '))
print(f'Список простых множителей числа {number}: {simple_mult(number)}')
