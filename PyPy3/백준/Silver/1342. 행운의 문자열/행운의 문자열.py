import sys
from collections import Counter

input = sys.stdin.readline

s = input().strip()
counter = Counter(s)
n = len(s)

def dfs(prev, depth):
    if depth == n:
        return 1

    total = 0
    for ch in counter:
        if counter[ch] == 0:
            continue
        if ch == prev:
            continue

        counter[ch] -= 1
        total += dfs(ch, depth + 1)
        counter[ch] += 1

    return total

print(dfs('', 0))