import sys
from collections import deque
input=sys.stdin.readline

def bfs(x,y):
    dx=[1,0,-1,0]   # 오른쪽, 위, 왼쪽, 아래
    dy=[0,1,0,-1]

    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M and arr[nx][ny]==1:
                queue.append((nx,ny))
                arr[nx][ny]=arr[x][y]+1

                if nx==N-1 and ny==M-1:
                    return arr[N-1][M-1]
    return -1

######################################################################

N,M=map(int, input().split())

arr=[]

for _ in range(N):
    A=list(map(int,list(input().strip())))
    arr.append(A)

print(bfs(0,0))