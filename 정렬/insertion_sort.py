import random

a = [random.randint(1,100) for i in range(10)]
b = a.copy()
def insertion_sort(list):
    length = len(list)
    for i in range(length):
        tmp = list[i]
        for j in range(
