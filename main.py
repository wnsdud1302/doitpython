
def main1():
    print("세정수의 최댓값을 구합니다.")
    a = input("a : ")
    b = input("b : ")
    c = input("c : ")
    max = a
    if b > max:
        max = b
    elif c > max:
        max = c
    print('최대값은 ', max, '입니다.')
    return 0


def main2():
    i = 0
    sum = 0
    print("1부터 n까지의 숫자합을 구합니다.")
    n = int(input("n : "))
    while i < n:
        sum  = sum + i
        i = i+1

    print("1부터", n, '까지의 합은 ', sum,'입니다.')

    return 0

def mian3():
    print(" 2자리 정수를 입력하세요")
    while True:
        num = int(input("수는 : "))
        if num  > 10 or num > 99:
            print("변수 num은 ",num,"이 되었습니다.")
            continue
        break

def main4():
    print("-----곱셈표-----")
    for i in range (1,9):
        print(i, end=" ")
        for j in range (1,9):
            print(i*j, end=" ")
        print(" ")

def main5():
    
    print("사각형을 출력합니다.")
    num = int(input("입력할 수: "))
    for i in range(0, num):
        for j in range(0, num):
            print("*", end="")
        print(" ")

def main6():
    print("삼각형을 출력합니다.")
    
    while True:
        num = int(input("몇단 삼각형입니까: "))
        if num <= 0: 
            continue
        break
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*", end="")
        print(" ")

def main7():
    while True:
        num = int(input("몇단 삼각형입니까: "))
        if num <= 0: 
            continue
        break
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            print("*", end="")
        print(" ")

def main8():
    print("삼각형을 출력합니다.")
    
    while True:
        num = int(input("몇단 삼각형입니까: "))
        if num <= 0: 
            continue
        break
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*", end="")
        print(" ")
main8()