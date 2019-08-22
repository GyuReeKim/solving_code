num = int(input())
for n in range(num):
    a, b = list(map(int, input().split()))
    print('#{0} {1} {2}'.format(n+1, a//b, a%b))