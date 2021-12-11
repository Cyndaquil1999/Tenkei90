N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split())) + [L]
diff = [A[0]]
for i in range(N): diff.append(A[i+1] - A[i])
 
def f(X):
    tmp = 0
    cnt = 0
    for i in diff:
        tmp += i
        if tmp >= X:
            tmp = 0
            cnt += 1
    return cnt
 
def binary_search(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if f(mid) >= K+1:
            ok = mid
        else:
            ng = mid
    return ok
 
print(binary_search(L+1,-1))
