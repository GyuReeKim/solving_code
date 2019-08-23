def change(a):
    A = list(zip(*a[::-1]))
    
    result = []
    for i in range(N):
        result.append(''.join(A[i]))
    return result
    


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    arr1 = change(arr)
    arr2 = change(arr1)
    arr3 = change(arr2)
    # print(change(arr))
    # print(change(arr1))
    # print(change(arr2))

    result = [arr1, arr2, arr3]
    # print(result)

    result = list(map(list, zip(*result)))
    # print(result)
    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(result[i]))