T = int(input())
for tc in range(1, T+1):
    # N = 5
    # M = 2
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # for i in range(N-M+1):
    #     for j in range(N-M+1):
    #         add = []
    #         for k in range(i, i+M):
    #             add.append(arr[k][j:j+M])
    #         print(add)

    add_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            add = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    add += arr[k][l]
            # print(add)
            if add > add_max:
                add_max = add
    print('#{} {}'.format(tc, add_max))


