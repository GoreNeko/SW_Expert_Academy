# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

T = int(input())
for test_case in range(1, T + 1):
    n = list(map(int, input().split()))
    sum = 0
    for i in range(10):
        sum = sum + n[i]

    avg = round(sum/10)
    print('#{0} {1}'.format(test_case, avg))