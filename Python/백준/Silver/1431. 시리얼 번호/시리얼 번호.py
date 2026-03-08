import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [input().strip() for _ in range(n)]

def digit_sum(s):
    total = 0
    for c in s:
        if c.isdigit():
            total += int(c)
    return total

arr.sort(key=lambda x: (len(x), digit_sum(x), x))

for s in arr:
    print(s)