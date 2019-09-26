T = 10
for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    add1 = 0
    add2 = 0
    maxV = 0
    for i in range(100):
        row = 0
        col = 0
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
            if i == j:
                add1 += arr[i][j]
            if i + j == 4:
                add2 += arr[i][j]
        if row > maxV:
            maxV = row
        if col > maxV:
            maxV = col
    if add1 > maxV:
        maxV = add1
    if add2 > maxV:
        maxV = add2
    print('#{} {}'.format(tc, maxV))