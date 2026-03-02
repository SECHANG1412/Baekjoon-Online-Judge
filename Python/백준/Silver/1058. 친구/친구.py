import sys
input = sys.stdin.readline

n = int(input().strip())
g = [list(input().strip()) for _ in range(n)]

ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if g[i][j] == 'Y':
            cnt += 1
        else:
            ok = False
            for k in range(n):
                if k != i and k != j and g[i][k] == 'Y' and g[k][j] == 'Y':
                    ok = True
                    break
            if ok:
                cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)