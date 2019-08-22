T = int(input())
for tc in range(1, T+1):
    word = input()
    if word == word[::-1]:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
