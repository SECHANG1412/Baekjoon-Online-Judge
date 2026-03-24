import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
dasom = int(input().strip())

if n == 1:
    print(0)
    exit()

hq = []
for _ in range(n - 1):
    votes = int(input().strip())
    heapq.heappush(hq, -votes)

cnt = 0

while hq and -hq[0] >= dasom:
    top = -heapq.heappop(hq)
    top -= 1
    dasom += 1
    cnt += 1
    heapq.heappush(hq, -top)

print(cnt)