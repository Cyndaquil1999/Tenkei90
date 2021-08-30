N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

Mod_a = [0]*46
Mod_b = [0]*46
Mod_c = [0]*46

for i in range(N):
    Mod_a[A[i]%46] += 1
    Mod_b[B[i]%46] += 1
    Mod_c[C[i]%46] += 1

cnt = 0

for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                cnt += Mod_a[i] * Mod_b[j] * Mod_c[k]
            

print(cnt)
