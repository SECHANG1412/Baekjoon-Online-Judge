import sys
input = sys.stdin.readline

n = int(input().strip())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

cards = list(range(n))
target = [i % 3 for i in range(n)]

visited = set()

def is_ok(c):
    for i in range(n):
        if P[c[i]] != target[i]:
            return False
    return True

cnt = 0

while True:
    t = tuple(cards)
    if t in visited:
        print(-1)
        break
    visited.add(t)

    if is_ok(cards):
        print(cnt)
        break

    new_cards = [0] * n
    for i in range(n):
        new_cards[S[i]] = cards[i]
    cards = new_cards

    cnt += 1