import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)
dist[1] = 0

q = deque([1])
while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

max_dist = max(dist)
barn = dist.index(max_dist)
count = dist.count(max_dist)

print(barn, max_dist, count)