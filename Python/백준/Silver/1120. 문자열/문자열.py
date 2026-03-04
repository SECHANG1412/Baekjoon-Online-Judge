import sys
input = sys.stdin.readline

a, b = input().split()
la, lb = len(a), len(b)

best = la 

for start in range(lb - la + 1):
    diff = 0
    for i in range(la):
        if a[i] != b[start + i]:
            diff += 1
    if diff < best:
        best = diff

print(best)