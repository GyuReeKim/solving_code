T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            row = ''
            col = ''
            for n in range(j, j+N):
                row += arr[i][n]
                col += arr[n][i]
            if row == row[::-1]:
                cnt += 1
            if col == col[::-1]:
                cnt += 1

    print('#{} {}'.format(tc, cnt))