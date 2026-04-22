import sys

input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))
else:
    one = min(dice)

    two_cases = [
        (0, 1), (0, 2), (0, 3), (0, 4),
        (5, 1), (5, 2), (5, 3), (5, 4),
        (1, 2), (1, 3), (4, 2), (4, 3)
    ]
    two = min(dice[i] + dice[j] for i, j in two_cases)

    three_cases = [
        (0, 1, 2), (0, 1, 3), (0, 4, 2), (0, 4, 3),
        (5, 1, 2), (5, 1, 3), (5, 4, 2), (5, 4, 3)
    ]
    three = min(dice[i] + dice[j] + dice[k] for i, j, k in three_cases)

    count_three = 4
    count_two = 8 * N - 12
    count_one = 5 * N * N - 16 * N + 12

    print(three * count_three + two * count_two + one * count_one)