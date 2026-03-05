import sys
input = sys.stdin.readline

n = int(input().strip())
r, g, b = map(int, input().split())
dp0, dp1, dp2 = r, g, b 

for _ in range(n - 1):
    r, g, b = map(int, input().split())
    ndp0 = r + (dp1 if dp1 < dp2 else dp2)
    ndp1 = g + (dp0 if dp0 < dp2 else dp2)
    ndp2 = b + (dp0 if dp0 < dp1 else dp1)
    dp0, dp1, dp2 = ndp0, ndp1, ndp2

print(dp0 if dp0 < dp1 and dp0 < dp2 else (dp1 if dp1 < dp2 else dp2))