T = 10
for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))

    cnt = 0
    while cnt < N:
        max_box = max(box)
        min_box = min(box)
        max_idx = 0
        min_idx = 0
        for i in range(len(box)):
            if box[i] == max_box:
                max_idx = i
            if box[i] == min_box:
                min_idx = i
        box[max_idx] -= 1
        box[min_idx] += 1
        cnt += 1
    diff = max(box) - min(box)
    print('#{} {}'.format(tc, diff))