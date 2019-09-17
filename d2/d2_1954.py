T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))
    
    for i in range(len(num), 0, -1):
        for i in range(i-1):
            if num[i] > num[i+1]:
                temp = num[i]
                num[i] = num[i+1]
                num[i+1] = temp
    
    add = 0
    for i in range(1, len(num)-1):
        add += num[i]

    result = round(add/(len(num)-2))
    print('#{} {}'.format(tc, result))