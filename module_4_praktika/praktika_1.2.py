
from math import sin;from datetime import datetime
from module_4_praktika.alg import *

data_1 = list(map(int, input('Введите числа через пробел').split()))
data_2 = list(map(int, input('Введите числа через пробел').split()))
data_3 = list(map(int, input('Введите числа через пробел').split()))

bubble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)

print(data_1)
print(data_2)
print(data_3)
