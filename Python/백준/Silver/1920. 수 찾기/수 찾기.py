import sys
input = sys.stdin.readline

def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2  
        if array[mid] == target:  
            return 1
        elif array[mid] < target:  
            left = mid + 1
        else:                      
            right = mid - 1

    return 0  

N = int(input())                        
A = sorted(map(int, input().split()))  
M = int(input())                        
targets = list(map(int, input().split()))

for t in targets:
    print(binary_search(A, t))