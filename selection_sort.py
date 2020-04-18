import random
a = [random.randint(1,100) for i in range(10)]
b = a.copy()
print(a)
def selection_sort(list):
    for i in range(0, len(list)-1):
        min = i
        for j in range(i+1,len(list)):
            if list[min] > list[j]:
                list[j],list[min] = list[min],list[j]

def selection_sort2(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
            list[i],list[min] = list[min],list[i]

selection_sort(a)
selection_sort2(b)
print(b)          
print(a)        