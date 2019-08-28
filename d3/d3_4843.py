T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers)
    numbers = [str(number) for number in numbers]

    result = []
    for i in range(10):
        if i % 2:
            result.append(numbers.pop(0))
        else:
            result.append(numbers.pop())
    print('#{} {}'.format(tc, ' '.join(result)))