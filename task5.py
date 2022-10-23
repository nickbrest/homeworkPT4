# 5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.


def polynom_union(data_1, data_2):
    with open(data_1, "r", encoding="utf-8") as file_1, \
            open(data_2, "r", encoding="utf-8") as file_2:
        
        data_f1 = file_1.readlines()
        data_f2 = file_2.readlines()

        if len(data_f1) == len(data_f2):
            with open("result_union.txt", "a", encoding="utf-8") as file_3:
                for i, polytext in enumerate(data_f1):
                    file_3.write(f"{polytext[:-5]} + {data_f2[i]}")
        else:
            print("Количество строк в файлах не совпадает")


polynom_union("result1.txt", "result2.txt")
