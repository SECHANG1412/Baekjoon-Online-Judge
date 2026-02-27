import sys
input = sys.stdin.readline

n, m = map(int, input().split())

q = n // m
r = n - q * m

ans = 1

for _ in range(m - r):
    ans *= q
for _ in range(r):
    ans *= (q + 1)

print(ans)