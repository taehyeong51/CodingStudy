import sys

n,m = map(int,input().split(' '))
mat = [[0 for _ in range(100)] for _ in range(100)]
cnt = 1
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split(' '))

    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            mat[i][j] +=1

ans = 0

for i in range(100):
    for j in range(100):

        if mat[i][j] > m:
            ans += 1

print(ans)