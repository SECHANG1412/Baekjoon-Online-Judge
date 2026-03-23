import sys
input = sys.stdin.readline

A, B = map(int, input().split())

spf = [0] * (B + 1)
for i in range(2, B + 1):
    if spf[i] == 0:
        for j in range(i, B + 1, i):
            if spf[j] == 0:
                spf[j] = i

cnt = [0] * (B + 1)
for i in range(2, B + 1):
    cnt[i] = cnt[i // spf[i]] + 1


is_prime = [True] * (B + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(B ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, B + 1, i):
            is_prime[j] = False

answer = 0
for i in range(A, B + 1):
    if is_prime[cnt[i]]:
        answer += 1

print(answer)