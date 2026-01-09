import sys
input=sys.stdin.readline

exp= input().strip().split('-')

first = sum(map(int, exp[0].split('+')))

total = 0

for part in exp[1:]:
    total += sum(map(int, part.split('+')))

print(first - total)