def devide(N, n):
    global result
    result.append(str(N//n))
    N -= (N//n)*n
    return N


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = []
    N = devide(N, 50000)
    N = devide(N, 10000)
    N = devide(N, 5000)
    N = devide(N, 1000)
    N = devide(N, 500)
    N = devide(N, 100)
    N = devide(N, 50)
    N = devide(N, 10)

    print('#{}'.format(tc))
    print(' '.join(result))
