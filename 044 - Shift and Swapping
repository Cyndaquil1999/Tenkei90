from collections import deque

N,Q = map(int,input().split())
A = deque(map(int,input().split()))
for _ in range(Q):
    T,X,Y = map(int,input().split())
    if T == 1: A[X-1],A[Y-1] = A[Y-1],A[X-1]
    elif T == 2: A.rotate()
    else: print(A[X-1])
    
