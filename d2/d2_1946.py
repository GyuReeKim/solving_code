T = int(input())
for tc in range(1, T+1):
    N = int(input())

    result = ''
    for i in range(N):
        C, K = input().split()

        result += C*int(K)

    print('#{}'.format(tc))
    final = ''
    for i in range(len(result)):
        if i != 0 and i % 10 == 0:
            print(final)
            final = ''
        final += result[i]
    print(final)