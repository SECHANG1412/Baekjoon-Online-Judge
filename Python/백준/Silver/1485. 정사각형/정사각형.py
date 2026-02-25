import sys
input = sys.stdin.readline

def dist_sq(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx * dx + dy * dy

def is_square(points):
    dists = []

    for i in range(4):
        for j in range(i + 1, 4):
            dists.append(dist_sq(points[i], points[j]))

    dists.sort()

    if dists[0] == 0:
        return 0

    if not (dists[0] == dists[1] == dists[2] == dists[3]):
        return 0

    if dists[4] != dists[5]:
        return 0

    if dists[4] != dists[0] * 2:
        return 0

    return 1


def solve():
    t = int(input().strip())
    answers = []

    for _ in range(t):
        points = [tuple(map(int, input().split())) for _ in range(4)]
        answers.append(str(is_square(points)))

    print("\n".join(answers))


solve()