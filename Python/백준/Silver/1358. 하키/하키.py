import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())

ans = 0
r = h / 2

for _ in range(p):
    px, py = map(int, input().split())

    # 가운데 직사각형
    if x <= px <= x + w and y <= py <= y + h:
        ans += 1
        continue

    # 왼쪽 반원
    if (px - x) ** 2 + (py - (y + r)) ** 2 <= r ** 2:
        ans += 1
        continue

    # 오른쪽 반원
    if (px - (x + w)) ** 2 + (py - (y + r)) ** 2 <= r ** 2:
        ans += 1

print(ans)