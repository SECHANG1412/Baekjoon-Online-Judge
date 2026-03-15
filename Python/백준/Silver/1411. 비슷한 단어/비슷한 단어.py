import sys
input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]

def pattern(s):
    d = {}
    idx = 0
    res = []
    for c in s:
        if c not in d:
            d[c] = idx
            idx += 1
        res.append(d[c])
    return tuple(res)

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if pattern(words[i]) == pattern(words[j]):
            ans += 1

print(ans)