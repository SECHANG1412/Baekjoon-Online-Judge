from itertools import combinations

N = int(input())
result = []
for i in range(1, 11):
    for temp in combinations(range(0, 10), i):
        temp = list(temp)
        temp.sort(reverse=True)
        result.append(int("".join(map(str, temp))))


result.sort()

try:
    print(result[N])
except:
    print(-1)