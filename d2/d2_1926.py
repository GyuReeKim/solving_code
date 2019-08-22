N = int(input())

result = []
for n in range(1, N+1):
    n = str(n)
    number = ''
    count = 0
    for i in n:
        if i == '3' or i == '6' or i == '9':
            count += 1
        else:
            number += i

    if count != 0:
        result.append('-'*count)
    else:
        result.append(number)
    number = ''
    count = 0

print(' '.join(result))