n, m = map(int, input().split())
board = [input() for _ in range(n)]

result = []

for i in range(n - 7):
    for j in range(m - 7):
        draw1 = 0  # B 시작
        draw2 = 0  # W 시작

        for a in range(8):
            for b in range(8):
                current = board[i + a][j + b]

                if (a + b) % 2 == 0:
                    if current != 'B':
                        draw1 += 1
                    if current != 'W':
                        draw2 += 1
                else:
                    if current != 'W':
                        draw1 += 1
                    if current != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))
