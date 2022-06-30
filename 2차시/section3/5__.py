m = 1000
n = "2 3 10 "
n = n.replace(" ",'')
n = list(map(int,n))
num = 0
cnt = 0
for i in range(len(n)):
    for j in range(i,len(n)):
        num += n[j]
        if num == m:
            cnt += 1
            break
    num = 0
    
print(cnt)