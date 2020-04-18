import random

a = [9,5,7,2,6,7,4,2,1]
b = [9,5,7,2,6,7,4,2,1]
c = [9,5,7,2,6,7,4,2,1]
print(a)
def is_sorted1(list, len):
    for i in range(0, len-1):
        if list[i] > list[i+1]:
            return 0
        else: return 1

def is_sorted2(list, len):
    for i in range(0,len-1):
        exchg = 0
        for j in range(len-1, 0, -1):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
                exchg = exchg + 1
        if exchg == 0:
            return 1
        else : return 0

def bubble_sort(list, n):
    for i in range(0, n-1):
        for j in range(n-1, 0, -1):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]

def bubble_sort_imporve1(list, n):
    for i in range(0,n-1):
        exchg = 0
        for j in range(n-1, 0, -1):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
                exchg = exchg + 1
        if exchg == 0:
            break

def bubble_sort_imporve2(list, n):
    k = 0
    while k < n-1 :
        last = n-1
        for j in range(n-1, k, -1):
            if list[j-1] > list[j]:
                list[j-1], list[j] = list[j], list[j-1]
            last = j
        k = last

def bubble_sort2(list):
    odd = 0
    even = 1
    shift = 0
    while odd or even <= len(list):
        break
bubble_sort2(a)
print(a)