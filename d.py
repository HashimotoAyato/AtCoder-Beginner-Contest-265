N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

l_sum, r_sum = 0, 0
L_SUM, R_SUM = [0], [0]
for i in range(N):
    l_sum += A[i]
    r_sum += A[N-1-i]
    L_SUM.append(l_sum)
    R_SUM.append(r_sum)
L_SUM.append(0)
R_SUM.append(0)
R_SUM.reverse()

print(L_SUM)
print(R_SUM)

target = sum(A)-(P+Q+R)
pairs = []
r = 1
for l in range(N):
    while R_SUM[r] > target - L_SUM[l]:
        if r < N-1:
            r += 1
        else:
            break
    if R_SUM[r] + L_SUM[l] == target:
        pairs.append([l+2, r])


for i in range(len(pairs)):
    sum = 0
    check1 = check2 = check3 = False
    