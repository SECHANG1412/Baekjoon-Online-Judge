import sys
input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]
length = len(words[0])

for l in range(1, length + 1):
    seen = set()
    for word in words:
        suffix = word[-l:]
        if suffix in seen:
            break
        seen.add(suffix)
    else:
        print(l)
        break