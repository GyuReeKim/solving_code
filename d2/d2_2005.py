T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    print('#{}'.format(tc))

    result = []
    for i in range(N):
        if i == 0:
            result.append('1')
            print(' '.join(result))
        elif i == 1:
            result.append('1')
            print(' '.join(result))
        else:
            middle = []
            for k in range(i-1):
                middle.append(str(int(result[k]) + int(result[k+1])))
            result = [result[0]] + middle + [result[-1]]
            print(' '.join(result))