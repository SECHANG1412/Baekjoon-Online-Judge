import sys
input = sys.stdin.readline

n = int(input().strip())
switch = [0] + list(map(int, input().split()))

m = int(input().strip())

for _ in range(m):
    gender, num = map(int, input().split())

    if gender == 1:  
        for i in range(num, n + 1, num):
            switch[i] ^= 1
    else:  
        left = right = num
        while left > 1 and right < n and switch[left - 1] == switch[right + 1]:
            left -= 1
            right += 1
        for i in range(left, right + 1):
            switch[i] ^= 1

for i in range(1, n + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()