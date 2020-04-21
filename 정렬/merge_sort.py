def merge_sort(list1, list2,list3):
    i = int()
    j = int()
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            list3.append(list2[j])
            j = j + 1
        elif list1[i] < list2[j]:
            list3.append(list1[i])
            i = i + 1
        else :
            list3.append(list1[i])
            i = i + 1
            j = j + 1
    while i < len(list1):
        list3.append(list1[i])
        i = i + 1
    while j < len(list2):
        list3.append(list2[j])
        j = j + 1

a = list(random.randint(1,50) for i in range(0,10))
b = list(random.randint(1,50) for i in range(0,10))
c = list()
a.sort()
b.sort()
print("리스트 a : ",a)
print("리스트 b : ",b)
merge_sort(a,b,c)
print("리스트 c ", c)
print(len(c))
