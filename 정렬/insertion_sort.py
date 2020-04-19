import random

a = [random.randint(1,100) for i in range(10)]
b = a.copy()
print("list a : ", a)
print("list b : ", b)
def insertion_sort1(list):
    length = len(list)
    for i in range(length):
        tmp = list[i]
        j = i
        while j > 0 and list[j-1] > tmp:
            list[j] = list[j-1]
        list[j] = tmp

def insertion_sort2(list):
	length = len(list)
	for i in range(length):
		key = list[i]
		pl = int()
		pr = i - 1
		pc = int()
		pd = int()
		while True:
			pc = (pl+pr) // 2
			if list[pc] == key:
				return pc
			elif list[pc] < key:
				pl = pc + 1
			elif list[pc] > key:
				pr = pc - 1
			if pl <= pr: continue
			break
		if pl <= pr : pd = pc + 1
		else : pd = pr + 1
		for j in range(i , pd, -1):
			list[j] = list[j-1]
		list[pd] = key
		
insertion_sort1(a)
insertion_sort2(b)
print("정렬된 리스트 : ", a)
print("정렬된 리스트 : ", b)
