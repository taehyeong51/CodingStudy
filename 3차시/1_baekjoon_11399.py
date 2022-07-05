# Baekjoon 11399

from sys import stdin
N = int(stdin.readline())
Pi = list(map(int, stdin.readline().split()))
Pi.sort()
ans = 0
for i in range(N):
    ans += sum(Pi[:i+1])
print(ans)
