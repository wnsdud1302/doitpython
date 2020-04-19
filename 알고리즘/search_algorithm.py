def max(list):
    max = list[0]
    for i in range(0,len(list)):
        if list[i > list[0]]:
            max = list[i]
    print(max)

def search(list, len, key):
    for i in range(0, len):        
        if list[i] == key:
            return i

def bin_search(list, len, key):
    pl = 0
    pr = len-1
    pc = 0
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
def bin_search2(list, len, key):
    pl = 0
    pr = len-1
    pc = 0
    i = 1
    while True:
        pc = (pl+pr) // 2
        if list[pc] == key:
           while True:
                
                if list[pc-i] != key:
                    return pc-i+1
                i=i+1
                if pc-i >= pl: continue
                break
        elif list[pc] < key:
            pl = pc + 1
        elif list[pc] > key:
            pr = pc - 1
        
        if pl <= pr: continue
        break

a = [1,3,5,7,7,7,7,8,8,9,9]
print(bin_search(a,len(a),7))
print(bin_search2(a,len(a),7))
   
