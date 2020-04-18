import random
a = list(random.randint(1,50) for i in range(0,8))
print(a)
def selection_sort(list):
    for i in range(0, len(list)-1):
        min = i
        for j in range(i+1,len(list)):
            if list[j] < list[min]:
                min = j
            list[i],list[min] = list[min],list[i]
selection_sort(a)          
print(a)        