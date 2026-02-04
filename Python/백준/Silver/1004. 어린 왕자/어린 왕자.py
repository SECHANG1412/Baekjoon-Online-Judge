import math
cases = int(input())
results = []

for case in range(cases):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    ps = int(input())
    planets = []
    for p in range(ps):
        px, py, pr = map(int, input().split())
        d1 = math.sqrt((x1 - px) ** 2 + (y1 - py) ** 2)
        d2 = math.sqrt((x2 - px) ** 2 + (y2 - py) ** 2)
        
        if d1 < pr or d2 < pr:
            if d1 < pr and d2 < pr: pass
            else: count += 1
                
    results.append(count)

for result in results:
    print(result)