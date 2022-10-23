# 1. Вычислить число c заданной точностью d


from decimal import Decimal


def accu(num, acc):
    number = Decimal(num)
    return number.quantize(Decimal(acc))


number = input('Введите число: ')
accuracy = input('Введите требуемую точность 0.0001: ')
print(accu(number, accuracy))
