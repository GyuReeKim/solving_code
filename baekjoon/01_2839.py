N = int(input())
kg_3 = N // 3
kg_5 = N // 5
result = []
for t in range(0, kg_3+1):
    for f in range(0, kg_5+1):
        if t*3 + f*5 == N:
            result.append(t + f)
        else:
            result.append(-1)
else:
    result.append(-1)

plus_result = []
for r in result:
    if r != -1:
        plus_result.append(r)
# print(plus_result)
if len(plus_result) == 0:
    print(-1)
else:
    print(min(plus_result))