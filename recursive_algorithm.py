def factorial(n):
    if n > 0: return n*factorial(n-1)
    else: return 1

def great_common_divisor(n1, n2):
    if n2 == 0: return n1
    else : return great_common_divisor(n2, n1 % n2)

def recur(n):
    if n > 0:
        recur(n-1)
        print(n)
        recur(n-2)

def move(n, x, y): #하노이 탑
    if n > 1:
        move(n-1, x, 6-x-y)
    print("원반",n,"을",x,"기둥에서 ",y,"기둥으로 옮김")
    if n > 1:
        move(n-1, 6-x-y, y)

pos = list(0 for i in range(0,8)) # 각열의 퀸 위치
flag_a = list(0 for i in range(0,8)) # 각행의 퀸 확인
flag_b = list(0 for i in range(0,15)) # /대각선의 퀸 확인
flag_c = list(0 for i in range(0,15)) # \대각선의 퀸 확인

def set(i):
        for j in range(0,8):
                if flag_a[j] == 0 and flag_b[i+j] == 0 and flag_c[i-j+7] == 0:
                        pos[i] = j
                        if i == 7:
                                print(pos)
                        else : 
                                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = 1
                                set(i+1)
                                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = 0
