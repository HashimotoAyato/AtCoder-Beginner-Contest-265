H, W = map(int, input().split())
G = [list(input()) for i in range(H)]
F = [[False for j in range(W)] for i in range(H)]

# init
y, x = 0, 0
F[y][x] = True

check = True
# main loop
while True:
    if G[y][x] == 'R':
        x += 1
    elif G[y][x] == 'L':
        x -= 1
    elif G[y][x] == 'U':
        y -= 1
    else:
        y += 1

    if 0 <= x < W and 0 <= y < H:
        if F[y][x]:
            check = False
            break
        else:
            F[y][x] = True
            continue
    else:
        x = max(min(x, W-1), 0)
        y = max(min(y, H-1), 0)
        break



if check:
    print(y+1, x+1)
else:
    print(-1)