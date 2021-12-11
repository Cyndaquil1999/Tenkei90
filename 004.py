H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
B = [0]*H
C = [0]*W
ans = [[0]*W for _ in range(H)]
 
for i in range(H):
    B[i] += sum(A[i])
 
tmp = 0
for i in range(W):
    for j in range(H):
        tmp += A[j][i]
    C[i] += tmp
    tmp = 0
 
for i in range(H):
    for j in range(W):
        ans[i][j] = B[i] + C[j] - A[i][j]
    
for i in range(H):
    print(*ans[i])
