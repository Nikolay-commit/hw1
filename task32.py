#  Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

from random import randint as rd # alias(псевдоним)
n = int(input("Введите кол-во элементов списка: "))
data_list = list()
for i in range(n):
    data_list.append(rd(-10, 10))
    min_value = 0
    max_value = 10
    filtered_indices = [index for index, value in enumerate(data_list) if min_value <= value <= max_value]
    print(filtered_indices)



