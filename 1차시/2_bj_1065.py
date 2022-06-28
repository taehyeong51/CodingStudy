n = int(input())
if n < 100:
    print(n)
elif n > 110:
    cnt = 0
    for i in range(111,n+1):
        if 2*int(str(i)[1]) == int(str(i)[0])+int(str(i)[2]):
            cnt += 1
    print(cnt+99)
else:
    print(99)