import sys
input=sys.stdin.readline

N,K=map(int, input().split())

coins=[]
cnt=0

for _ in range(N):
    coins.append(int(input()))
    coins.sort(reverse=True)

for coin in coins:
    cnt += K // coin    
    K %= coin

print(cnt)