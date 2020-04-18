def GuGu(a):
    result = []
    for i in range(1,10):
        result.append(a * i)
    print(result)
GuGu(2)

def add35():
    result = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 ==0:
            result = result + i 
    print(result)
add35()

def GetTotalPage(m, n):
    if m % n == 0:
        print(m//n)
    else:
        print(m//n +1)
GetTotalPage(23,10)
GetTotalPage(30,10)

Matrix = [[0]*5 for i in range(5)]

Matrix[1][0] = 1
Matrix[1][1] = 1



