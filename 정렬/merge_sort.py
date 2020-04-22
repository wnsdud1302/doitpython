import random
def __merge_sort(list1, list2,list3):
    while True:
        if list1 == None:
            while list2 != None:
                list3.append(list2.pop(0))
            break
        if list2 == None:
            while list1 != None:
                list3.append(list1.pop(0))
            break
        if list1[0] > list2[0]:
            list3.append(list2.pop(0))
            continue
        if list1[0] < list2[0]:
            list3.append(list1.pop(0))
            continue
        if list1[0] == list2[0]:
            list3.append(list1.pop(0))
            list3.append(list2.pop(0))
            continue
        


def merge_sort(exlist, sort_list):
    length = len(exlist)
    left_list = list()
    right_list = list()
    left = 0
    center = length//2
    right = center
    while left < center:
        left_list.append(exlist[left])
        left_list.sort()
        left = left + 1
    while right < length:
        right_list.append(exlist[right])
        right_list.sort()
        right = right + 1
    __merge_sort(left_list,right_list,sort_list)




a = list(random.randint(1,50) for i in range(0,10))
print("리스트 a : ",a)
merge_sort(a, a)
print("정렬된 리스트 a : ", a)
