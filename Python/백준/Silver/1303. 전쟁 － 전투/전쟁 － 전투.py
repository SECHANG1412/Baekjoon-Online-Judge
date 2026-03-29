import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = [input().strip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    color = board[x][y]
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

white = 0
blue = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            size = bfs(i, j)
            if board[i][j] == 'W':
                white += size * size
            else:
                blue += size * size

print(white, blue)