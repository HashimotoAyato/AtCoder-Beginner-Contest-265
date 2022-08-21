N, M, T = map(int, input().split())
A = list(map(int, input().split()))
B = [0 for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    B[x-1] = y
    
ans = True
for i in range(N-1):
    T -= A[i]
    if T <= 0:
        ans = False
        break
    T += B[i+1]

print('Yes' if ans else 'No')
