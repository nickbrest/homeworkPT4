# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.


from random import choice


def polynom(numb_k):
    if numb_k < 1:
        return 0

    string_polynom = ""
  
    with open("result.txt", "a", encoding="utf-8") as file:
        for i in range(numb_k, 0, -1):
            number = choice(range(0, 10))
            if number != 0:
                string_polynom += f"{number}*x^{i} {choice('+-')} "
        string_polynom += f'{choice(range(0, 10))} = 0'

        file.write(f"{string_polynom}\n")


polynom(int(input("Введите степень: ")))
polynom(int(input("Введите степень: ")))
polynom(int(input("Введите степень: ")))
