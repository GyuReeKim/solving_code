def devide(N, n):
    cnt = 0
    while N % n == 0:
        N = int(N/n)
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    a = devide(N, 2)
    b = devide(N, 3)
    c = devide(N, 5)
    d = devide(N, 7)
    e = devide(N, 11)

    print('#{} {} {} {} {} {}'.format(tc, a, b, c, d, e))