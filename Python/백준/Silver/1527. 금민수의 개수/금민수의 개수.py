import sys
input = sys.stdin.readline

a, b = map(int, input().split())

ans = 0

def dfs(num):
    global ans
    if num > b:
        return
    if num >= a:
        ans += 1
    dfs(num * 10 + 4)
    dfs(num * 10 + 7)

dfs(4)
dfs(7)

print(ans)