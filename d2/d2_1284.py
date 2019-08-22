Test = int(input())
for tc in range(1, Test+1):
    P, Q, R, S, W = list(map(int, input().split()))

    A = P * W

    if R >= W:
        B = Q
    else:
        B = Q + (W - R) * S

    if A > B:
        print('#{} {}'.format(tc, B))
    else:
        print('#{} {}'.format(tc, A))