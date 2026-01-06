import sys
import heapq  
input = sys.stdin.readline

n = int(input()) 
heap = []  

for _ in range(n):
    x = int(input())  

    if x != 0:
        heapq.heappush(heap, (abs(x), x))

    else:
        if heap:  
            abs_val, real_val = heapq.heappop(heap)
            print(real_val)
        else:
            print(0)  
