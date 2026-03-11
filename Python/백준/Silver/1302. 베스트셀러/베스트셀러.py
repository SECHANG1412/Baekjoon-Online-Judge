import sys
input = sys.stdin.readline

n = int(input().strip())
d = {}

for _ in range(n):
    book = input().strip()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

max_cnt = max(d.values())

ans = []
for k, v in d.items():
    if v == max_cnt:
        ans.append(k)

ans.sort()
print(ans[0])