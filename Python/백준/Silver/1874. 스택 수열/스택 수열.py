import sys
input = sys.stdin.readline

n = int(input()) 
sequence = [int(input()) for _ in range(n)] 

stack = []      
result = []      
current = 1      
possible = True  

for target in sequence:
    while current <= target:
        stack.append(current)   
        result.append('+')     
        current += 1          

    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')     
    else:
        possible = False
        break

if possible:
    print('\n'.join(result)) 
else:
    print('NO')
