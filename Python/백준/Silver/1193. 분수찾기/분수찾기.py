import sys
input = sys.stdin.readline

x = int(input().strip())

d = 1
s = 1
while s < x:
    d += 1
    s += d

pos = x - (s - d)  # 1..d

if d % 2 == 0:
    num = pos
    den = d - pos + 1
else:
    num = d - pos + 1
    den = pos

print(f"{num}/{den}")