import sys
input = sys.stdin.readline

n = int(input().strip())
ans = 0

for _ in range(n):
    word = input().strip()
    seen = set()
    prev = ''

    ok = True
    for c in word:
        if c != prev:
            if c in seen:
                ok = False
                break
            seen.add(c)
        prev = c

    if ok:
        ans += 1

print(ans)