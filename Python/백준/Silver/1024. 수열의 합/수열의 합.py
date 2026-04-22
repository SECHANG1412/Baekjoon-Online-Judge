import sys

N, L = map(int, sys.stdin.readline().split())

for length in range(L, 101):
    numerator = N - (length * (length - 1) // 2)
    
    if numerator < 0:
        continue
    
    if numerator % length == 0:
        start = numerator // length
        if start >= 0:
            for i in range(length):
                print(start + i, end=' ')
            break
else:
    print(-1)