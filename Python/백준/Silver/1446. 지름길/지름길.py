import sys
input = sys.stdin.readline

n, d = map(int, input().split())

shortcuts = [[] for _ in range(d + 1)]
for _ in range(n):
    s, e, l = map(int, input().split())
    if e <= d:
        shortcuts[s].append((e, l))

dp = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    for e, l in shortcuts[i]:
        if dp[e] > dp[i] + l:
            dp[e] = dp[i] + l

print(dp[d])