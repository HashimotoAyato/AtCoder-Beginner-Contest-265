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
        pairs.append([l+1, r])

for i in range(len(pairs)):
    check1 = False
    check2 = False
    sum = 0
    for j in range(pairs[i][0], pairs[i][1]+1):
        sum += A[j]
        if check1 == False and sum == P:
            check1 = True
        
        if check1 and sum == P+Q:
            check2 = True
            break
    if check1 and check2:
        break
    
print('Yes' if check1 and check2 else 'No')