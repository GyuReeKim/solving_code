T = int(input())
for tc in range(1, T+1):
    chars = input()
    word = ''
    for i in range(len(chars)):
        word += chars[i]
        if chars[i+1: i+len(word)+1] == word:
            break
    print('#{} {}'.format(tc, len(word)))