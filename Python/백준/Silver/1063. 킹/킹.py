import sys
input = sys.stdin.readline

king, stone, n = input().split()
n = int(n)

# 이동 방향
move = {
    'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
    'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)
}

def to_xy(pos):
    return ord(pos[0]) - ord('A'), int(pos[1]) - 1

def to_pos(x, y):
    return chr(x + ord('A')) + str(y + 1)

kx, ky = to_xy(king)
sx, sy = to_xy(stone)

for _ in range(n):
    cmd = input().strip()
    dx, dy = move[cmd]

    nkx, nky = kx + dx, ky + dy

    if not (0 <= nkx < 8 and 0 <= nky < 8):
        continue

    if nkx == sx and nky == sy:
        nsx, nsy = sx + dx, sy + dy
        if not (0 <= nsx < 8 and 0 <= nsy < 8):
            continue
        sx, sy = nsx, nsy

    kx, ky = nkx, nky

print(to_pos(kx, ky))
print(to_pos(sx, sy))