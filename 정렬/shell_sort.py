import random

a = list(random.randint(0,50) for i in range(0,20))
b = a.copy()
print("list a : ", a)
print("list b : ", b)

def shell_sort(list):
    length = len(list)
    h = int(len(list) / 2)
    while h > 0 :
        for i in range(int(h),length):
            tmp = list[i]
            j = i
            while j > 0 and list[j-int(h)] > tmp:
                list[j] = list[j-int(h)]
                j = j - int(h)
            list[j] = tmp
        h = h / 2

def shell_sort_improve1(list):
    h = int(1)
    length = len(list)
    while h < length / 9:
        h = h*3 + 1
    while h > 0:
        for i in range(int(h), length):
            tmp = list[i]
            j = i
            while j > 0 and list[j - int(h)] > tmp:
                list[j] = list[j-int(h)]
                j = j - int(h)
            list[j] = tmp
        h = h / 3


shell_sort(a)
shell_sort_improve1(b)
print("정렬된 리스트 : ",a)
print("정렬된 리스트 : ",b)

    


