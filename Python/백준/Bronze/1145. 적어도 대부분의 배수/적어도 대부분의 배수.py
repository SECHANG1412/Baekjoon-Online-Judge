import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))

x = min(nums)

while True:
    cnt = 0
    for num in nums:
        if x % num == 0:
            cnt += 1
    if cnt >= 3:
        print(x)
        break
    x += 1