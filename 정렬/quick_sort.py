import random
a = [random.randint(1,10) for i in range(0,10)]
print(a)
def quick_sort(list):
    if len(list) <= 1 : return list
    length = len(list)
    pivot = list[length//2]
    less, equal, big = [], [] ,[]
    for i in list:
        if i < pivot : less.append(i)
        elif i > pivot : big.append(i)
        else : equal.append(i)
    return quick_sort(less) + equal + quick_sort(big)
print(quick_sort(a))
