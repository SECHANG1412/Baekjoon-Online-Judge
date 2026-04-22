from collections import Counter
import sys

name = sys.stdin.readline().strip()
count = Counter(name)

odd = [ch for ch, cnt in count.items() if cnt % 2]

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    half = []
    mid = odd[0] if odd else ""

    for ch in sorted(count):
        half.append(ch * (count[ch] // 2))

    left = "".join(half)
    print(left + mid + left[::-1])