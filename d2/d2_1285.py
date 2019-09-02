T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rock = list(map(int, input().split()))

    minV = 100000
    for i in range(N):
        if abs(rock[i] - 0) <= minV:
            minV = abs(rock[i] - 0)
    # print(minV)

    count = 0
    for i in range(N):
        if abs(rock[i] - 0) == minV:
            count += 1
    print('#{} {} {}'.format(tc, minV, count))