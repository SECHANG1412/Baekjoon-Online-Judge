import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = []

for person in range(n, 0, -1):
    result.insert(arr[person - 1], person)

print(*result)