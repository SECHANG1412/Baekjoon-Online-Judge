import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [int(input().strip()) for _ in range(n)]

s = set(arr)
ans = 5

for x in arr:
    cnt = 0
    for i in range(5):
        if x + i in s:
            cnt += 1
    if 5 - cnt < ans:
        ans = 5 - cnt

print(ans)