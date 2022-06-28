import sys
n = int(sys.stdin.readline())
N = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
M = list(map(int,sys.stdin.readline().rstrip().split()))

s = set(M) - set(N)
ans = ''
for i in M:
    if i in s:
        ans += '0 '
    else:
        ans += "1 "

print(ans.rstrip())