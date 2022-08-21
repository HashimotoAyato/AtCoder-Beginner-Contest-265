X, Y, N = map(int, input().split())

ans = 0
n = 0
if 3*X < Y:
    n += N
    ans += N*X
else:
    n += int(N/3)*3
    ans += Y * int(N/3)
    ans += X * (N-n)
    n += N - n

print(ans)
    